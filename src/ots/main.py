from secrets import token_urlsafe

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/templates")

# Use a simple dictionary to store secrets
app_state = {}


async def secret_new(request: Request):
    async with request.form() as form:
        if form["secret"]:
            share_token = token_urlsafe(6)
            app_state[share_token] = form["secret"]
            return RedirectResponse(
                url=request.url_for("secret_share", share_token=share_token),
                status_code=303,
            )
    return RedirectResponse(url="/")


def secret_share(
    request: Request,
):
    return templates.TemplateResponse(
        name="share.html",
        context={
            "request": request,
            "share_token": request.path_params["share_token"],
        },
    )


def secret_preview(
    request: Request,
):
    return templates.TemplateResponse(
        name="preview.html",
        context={
            "request": request,
            "share_token": request.path_params["share_token"],
        },
    )


def secret_receive(
    request: Request,
):
    share_token = request.path_params["share_token"]
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


async def index(
    request: Request,
):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
        },
    )


routes = [
    Route("/", index),
    Route("/secret/receive/{share_token}", secret_receive),
    Route("/secret/{share_token}", secret_preview),
    Route("/secret/share/{share_token}", secret_share),
    Route("/secret/new/", secret_new, methods=["POST"]),
    Mount("/static", StaticFiles(directory="src/static"), name="static"),
]
app = Starlette(debug=True, routes=routes)
