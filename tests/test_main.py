import re


async def test_index(client):
    response = await client.get("/")
    assert response.status_code == 200
    assert b'<div class="error-alert">' in response.content


async def test_happy_path(client):
    secret = "testsecret"
    response = await client.post(
        "/secret/new/", data={"secret": secret}, follow_redirects=True
    )
    assert response.status_code == 200
    assert (
        b'class="secret-form" id="secret-link">http://testserver/secret/'
        in response.content
    )

    pattern = r'<div\s+class=["\']secret-form["\'][^>]*>http://[^/]+/secret/([A-Za-z0-9]+)</div>'
    match = re.search(pattern, response.content.decode())
    assert match is not None, "Secret token div not found in HTML content."
    token = match.group(1)
    response = await client.get(f"/secret/share/{token}")
    assert f"http://testserver/secret/{token}" in response.content.decode()
    response = await client.get(f"/secret/receive/{token}")
    assert secret in response.content.decode()
    response = await client.get(f"/secret/receive/{token}")
    assert "Hier ist kein one time secret (OTS)." in response.content.decode()
