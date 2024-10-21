from secrets import token_urlsafe

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# Use a simple dictionary to store secrets
app_state = {}


@app.post("/secret/new/")
async def secret_new(secret: str = Form()):
    if secret:
        share_uri = token_urlsafe(4)
        app_state[share_uri] = secret
        return RedirectResponse(url=f"/secret/share/{share_uri}", status_code=303)
    return {"secret": secret}


@app.get("/secret/share/{share_uri}", response_class=HTMLResponse)
def api_secret_share(
    request: Request,
    share_uri: str,
):
    return templates.TemplateResponse(
        name="share.html",
        context={
            "request": request,
            "share_uri": share_uri,
        },
    )


@app.get("/secret/receive/{share_uri}", response_class=HTMLResponse)
def api_secret_receive(
    request: Request,
    share_uri: str,
):
    # Retrieve and remove the secret from the dictionary
    secret = app_state.pop(share_uri, None)
    if secret:
        return templates.TemplateResponse(
            name="receive.html",
            context={
                "request": request,
                "otsecret": secret,
            },
        )
    else:
        return templates.TemplateResponse(
            name="receive.html",
            context={
                "request": request,
                "no_secret": True,
            },
        )


@app.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
        },
    )
