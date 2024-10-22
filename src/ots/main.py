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
        share_token = token_urlsafe(6)
        app_state[share_token] = secret
        return RedirectResponse(url=f"/secret/share/{share_token}", status_code=303)
    return {"secret": secret}


@app.get("/secret/share/{share_token}", response_class=HTMLResponse)
def secret_share(
    request: Request,
    share_token: str,
):
    return templates.TemplateResponse(
        name="share.html",
        context={
            "request": request,
            "share_token": share_token,
        },
    )


@app.get("/secret/{share_token}", response_class=HTMLResponse)
def secret_preview(
    request: Request,
    share_token: str,
):
    return templates.TemplateResponse(
        name="preview.html",
        context={
            "request": request,
            "share_token": share_token,
        },
    )


@app.get("/secret/receive/{share_token}", response_class=HTMLResponse)
def secret_receive(
    request: Request,
    share_token: str,
):
    # Retrieve and remove the secret from the dictionary
    secret = app_state.pop(share_token, None)
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
