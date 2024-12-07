import asyncio
from urllib.parse import urlencode

import pytest

from src.ots import (  # Replace with the actual name of your main code file
    app_state,
    get_css,
    get_logo,
    handle_request,
    html_base,
    html_index,
    html_preview,
    html_receive,
    html_share,
    main,
    response_200,
    response_404,
    response_redirect,
)


@pytest.mark.asyncio
async def test_handle_request_index():
    # Test the index route
    response = await handle_request("GET", "/", {}, b"")
    assert b"<html" in response
    assert b"aubex" in response


@pytest.mark.asyncio
async def test_handle_request_new_post():
    # Test posting a secret to "/new"
    secret_data = {"secret": "mysecret"}
    body = urlencode(secret_data).encode("utf-8")
    response = await handle_request(
        "POST", "/new", {"content-length": str(len(body))}, body
    )
    # Should redirect to something like /share/<token>
    assert response.startswith(b"HTTP/1.1 303 See Other")
    assert b"Location: /share/" in response


@pytest.mark.asyncio
async def test_handle_request_share():
    # First, create a token in the state
    share_token = "testtoken"
    app_state[share_token] = "sharedsecret"
    response = await handle_request("GET", f"/share/{share_token}", {}, b"")
    assert b"<html" in response
    assert b"testtoken" in response  # The share page might show the token to the user


@pytest.mark.asyncio
async def test_handle_request_receive():
    # Put a token in state so we can receive it
    share_token = "receivetoken"
    app_state[share_token] = "secretvalue"
    response = await handle_request("GET", f"/receive/{share_token}", {}, b"")
    assert b"secretvalue" in response
    # After receiving, the secret should be removed from state
    assert share_token not in app_state


@pytest.mark.asyncio
async def test_handle_request_preview():
    # If we just go to something like "/randomtoken", it shows a preview
    response = await handle_request("GET", "/randomtoken", {}, b"")
    # The preview might just show a placeholder if token isn't found
    assert b"<html" in response


@pytest.mark.asyncio
async def test_handle_request_404():
    response = await handle_request("GET", "", {}, b"")
    assert b"HTTP/1.1 404 Not Found" in response


def test_get_css_and_logo():
    # Assuming these return strings or some known non-empty values
    css_content = get_css()
    logo_content = get_logo()
    assert isinstance(css_content, str) and len(css_content) > 0
    assert isinstance(logo_content, str) and len(logo_content) > 0


def test_html_base():
    content = "<p>Hello</p>"
    result = html_base(content)
    assert "<html" in result and "</html>" in result
    assert "<p>Hello</p>" in result


def test_html_index():
    result = html_index()
    assert "<html" in result and "form" in result


def test_html_share():
    result = html_share("testtoken", {})
    assert "testtoken" in result


def test_html_preview():
    result = html_preview("sometoken")
    # Just checking that the token appears somewhere in the preview page
    assert "sometoken" in result


def test_html_receive():
    # Test receiving a known secret
    result = html_receive("secretvalue")
    assert "secretvalue" in result
    # Test receiving with None
    result = html_receive(None)
    assert "Hier ist kein one time secret (OTS)" in result or "not available" in result


def test_response_200():
    resp = response_200("<html></html>")
    assert resp.startswith(b"HTTP/1.1 200 OK")


def test_response_404():
    resp = response_404()
    assert resp.startswith(b"HTTP/1.1 404 Not Found")


def test_response_redirect():
    resp = response_redirect("/somewhere")
    assert resp.startswith(b"HTTP/1.1 303")
    assert b"Location: /somewhere" in resp


@pytest.mark.asyncio
async def test_main():
    # Testing main directly might be more integration-level testing.
    # For simplicity, just ensure it doesn't fail immediately.
    # We won't actually run the server fully here.
    # If you needed a full integration test, you'd start main in the background and simulate requests.
    task = asyncio.create_task(main("127.0.0.1", 8001))
    # Give the server a moment to start
    await asyncio.sleep(0.1)
    task.cancel()  # Stop the server immediately to confirm it started without error
    with pytest.raises(asyncio.CancelledError):
        await task
