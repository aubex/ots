import asyncio

import httpx
import pytest

from src.ots import main  # Replace with your actual module


@pytest.fixture
async def app():
    # Start the server as a background task.
    # Adjust host/port as needed; this must match what your server is configured to listen on.
    host = "127.0.0.1"
    port = 8001

    # Create a task to run the server.
    server_task = asyncio.create_task(main(host, port))

    # Give the server a moment to start.
    await asyncio.sleep(0.1)

    # Yield control back to the test.
    yield f"http://{host}:{port}"

    # After the test, cancel the server task.
    server_task.cancel()
    # Ensure the task finishes cleanly.
    with pytest.raises(asyncio.CancelledError):
        await server_task


@pytest.mark.asyncio
async def test_index_page(app):
    base_url = app
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/")
        assert response.status_code == 200
        # Check the response body for expected content.
        assert (
            """<h1>OpenSource one time secret (OTS) sharing tool by aubex, Hockenheim.</h1>
<p>Dies ist ein extrem simples and kleines tool zum sicheren Austausch von Geheimnissen wie Passwörtern, z.B. während eines Meetings.</p>
<form action="/new/" class="secret-form" method="post">
    <div>
        <label for="secret">Neues Geheimnis:</label>
        <input type="text" name="secret" id="secret" required="">
    </div>
    <div id="submit">
        <input type="submit" value="Teilen!" />
    </div>
</form>"""
            in response.text
        )


@pytest.mark.asyncio
async def test_post_new_secret(app):
    base_url = app
    async with httpx.AsyncClient() as client:
        # POST a secret to /new
        response = await client.post(f"{base_url}/new", data={"secret": "mysecret"})
        # Expect a redirect to something like /share/<token>
        assert response.status_code == 303
        assert "Location" in response.headers
        assert "/share/" in response.headers["Location"]

        # Optionally, follow the redirect to ensure the share page is accessible.
        share_url = response.headers["Location"]
        share_response = await client.get(f"{base_url}{share_url}")
        assert share_response.status_code == 200
        assert (
            "mysecret" not in share_response.text
        )  # The share page might just show instructions, not the secret itself.


@pytest.mark.asyncio
async def test_receive_secret(app):
    base_url = app
    async with httpx.AsyncClient() as client:
        # First, store a secret by posting to /new
        post_response = await client.post(
            f"{base_url}/new", data={"secret": "mysecret"}
        )
        assert post_response.status_code == 303
        share_url = post_response.headers["Location"]

        # Extract the token from the share_url, for example "/share/ABC123"
        token = share_url.split("/")[-1]

        # Accessing /receive/<token> should return the secret once, then remove it.
        receive_response = await client.get(f"{base_url}/receive/{token}")
        assert receive_response.status_code == 200
        assert "mysecret" in receive_response.text

        # A second try should not have the secret available anymore.
        second_response = await client.get(f"{base_url}/receive/{token}")
        assert second_response.status_code == 200
        assert "mysecret" not in second_response.text
