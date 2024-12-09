import asyncio
import base64
import json
from secrets import token_urlsafe
from typing import Dict
from urllib.parse import parse_qs


def get_css() -> str:
    return """
/* https://github.com/Lazzzer00/Best-CSS-Reset-2024/blob/main/css_reset.css */
*,
*::before,
*::after {
    box-sizing: border-box;
}

* {
    margin: 0;
    padding: 0;
}

ul[role='list'],
ol[role='list'] {
    list-style: none;
}

html:focus-within {
    scroll-behavior: smooth;
}

a:not([class]) {
    text-decoration-skip-ink: auto;
}

img,
picture,
svg,
video,
canvas {
    max-width: 100%;
    height: auto;
    vertical-align: middle;
    font-style: italic;
    background-repeat: no-repeat;
    background-size: cover;
}

input,
button,
textarea,
select {
    font: inherit;
}

@media (prefers-reduced-motion: reduce) {
    html:focus-within {
        scroll-behavior: auto;
    }

    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
        transition: none;
    }
}

body,
html {
    height: 100%;
    scroll-behavior: smooth;
}

/* end css reset */

body {
    background-color: #ECF0F1;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    color: #34495E;
    margin: 0;
    padding: 0;
    display: grid;
    grid-template-rows: 20% 1fr 20%;
    justify-items: center;
}

.error-alert {
    position: fixed;
    pointer-events: none;
    z-index: 100;
    height: 100%;
    width: 100%;
    border: 1rem solid red;
    color: red;
}

#content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 1rem;
}

h1 {
    color: #2C3E50;
    text-align: center;
    padding-top: 30px;
    line-height: 1.8rem;
    font-size: 1.4rem;
}

p {
    max-width: 600px;
    margin: 10px auto;
    text-align: center;
    line-height: 1.4rem;
    font-size: 1rem;
}

.secret-form {
    background-color: #FFFFFF;
    max-width: 500px;
    width: 100%;
    margin: 20px auto;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

#submit {
    text-align: center;
}

label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
}

input[type="text"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #BDC3C7;
    border-radius: 4px;
}

input[type="submit"] {
    background-color: #1ABC9C;
    color: #FFFFFF;
    border: none;
    padding: 12px 20px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

input[type="submit"]:hover {
    background-color: #16A085;
}

.logo {
    width: 10rem;
    align-self: end;
}

.button {
    background-color: #1ABC9C;
    /* Teal color for empathy */
    color: #FFFFFF;
    /* White text for readability */
    border: none;
    padding: 12px 24px;
    border-radius: 5px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s ease, transform 0.2s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.button:hover {
    background-color: #16A085;
    /* Slightly darker teal on hover */
}

.button:active {
    background-color: #149174;
    /* Even darker teal when clicked */
    transform: translateY(2px);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.button:focus {
    outline: none;
    box-shadow: 0 0 0 3px rgba(26, 188, 156, 0.4);
}

#footer {
    align-self: end;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    line-height: 1.4rem;
    font-size: 1rem;
}

#footer p {
    line-height: 1.4rem;
    font-size: 1rem;
}
"""


def get_logo() -> str:
    return base64.b64encode(
        """<svg id="Ebene_1" data-name="Ebene 1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 2500 1000"><defs><style>.cls-1{fill:url(#Unbenannter_Verlauf_5);}.cls-2{fill:url(#Unbenannter_Verlauf_5-2);}.cls-3{fill:url(#Unbenannter_Verlauf_5-3);}.cls-4{fill:url(#Unbenannter_Verlauf_5-4);}.cls-5{fill:url(#Unbenannter_Verlauf_5-5);}</style><linearGradient id="Unbenannter_Verlauf_5" x1="-268.22" y1="992.92" x2="-209.68" y2="992.92" gradientTransform="matrix(42.05, 0, 0, -41.13, 11300.47, 41391.2)" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#3eace5"/><stop offset="0.2" stop-color="#56bbd0"/><stop offset="1" stop-color="#ffe732"/></linearGradient><linearGradient id="Unbenannter_Verlauf_5-2" x1="-271.18" y1="992.92" x2="-207.63" y2="992.92" gradientTransform="matrix(38.73, 0, 0, -41.13, 10523.85, 41393.84)" xlink:href="#Unbenannter_Verlauf_5"/><linearGradient id="Unbenannter_Verlauf_5-3" x1="-270.59" y1="996.43" x2="-211.97" y2="996.43" gradientTransform="matrix(41.99, 0, 0, -57.28, 11382.78, 57545.54)" xlink:href="#Unbenannter_Verlauf_5"/><linearGradient id="Unbenannter_Verlauf_5-4" x1="-275.68" y1="992.92" x2="-206.89" y2="992.92" gradientTransform="matrix(35.79, 0, 0, -41.14, 9887.33, 41404.41)" xlink:href="#Unbenannter_Verlauf_5"/><linearGradient id="Unbenannter_Verlauf_5-5" x1="-272.67" y1="992.92" x2="-214.14" y2="992.92" gradientTransform="matrix(42.05, 0, 0, -41.12, 11487, 41378.77)" xlink:href="#Unbenannter_Verlauf_5"/></defs><g id="Gruppe_312" data-name="Gruppe 312"><g id="Gruppe_182" data-name="Gruppe 182"><path id="Pfad_253" data-name="Pfad 253" class="cls-1" d="M352,504.36q0-46.53-18.84-62.7t-73.75-16.11H53.78V331.12H259.36q54.93,0,76,2a207,207,0,0,1,42.31,8.59q100.58,38.12,95.7,182.09v249H217.24a750.3,750.3,0,0,1-95-4,112.77,112.77,0,0,1-46.3-17.29q-54-36.33-54-109.43a148.29,148.29,0,0,1,21.48-79.5,108.11,108.11,0,0,1,56.49-47.18q31-11.05,103.23-11.07Zm0,94.36H211.5l-20.41-.44a47.26,47.26,0,0,0-32.93,11.08A38.12,38.12,0,0,0,146,639a32.68,32.68,0,0,0,14.84,30.57,105.17,105.17,0,0,0,50.73,8.86H352Z"/><path id="Pfad_254" data-name="Pfad 254" class="cls-2" d="M862.58,678.47V331.12H984V772.85H744.72a325.93,325.93,0,0,1-80.19-7.52,119.06,119.06,0,0,1-50.08-27.93Q568,695.31,567.94,602.72V331.12H689.33v284a66,66,0,0,0,15.51,46.51,55.44,55.44,0,0,0,43,16.83Z"/><path id="Pfad_255" data-name="Pfad 255" class="cls-3" d="M1199.74,331.12H1307.4a262.82,262.82,0,0,1,115.18,21.71,178.63,178.63,0,0,1,87.29,91.71A257.89,257.89,0,0,1,1529.36,546q0,134.28-97.46,194.49A195,195,0,0,1,1368.75,766a481.84,481.84,0,0,1-92.82,6.87H1078.34V157.57h121.4Zm0,94.38v253h89.93q57.6,0,85.94-35.46a146.38,146.38,0,0,0,29.69-93.46q0-124.05-115.65-124.05Z"/><path id="Pfad_256" data-name="Pfad 256" class="cls-4" d="M1976.77,504.36v94.36h-250.1q3.54,43.42,28.14,61.59t79.49,18.15h142.47v94.37H1821a324.9,324.9,0,0,1-85.74-9.31,186.79,186.79,0,0,1-62.69-31.9q-80.2-62-80.2-185.19a234.17,234.17,0,0,1,42.53-140,165.49,165.49,0,0,1,70-58,278.52,278.52,0,0,1,107.21-17.29h164.65V425.5H1821q-49.63,0-69.83,16.83t-24.59,62Z"/><path id="Pfad_257" data-name="Pfad 257" class="cls-5" d="M2483,331.12H2349.63l-92.5,128.35-92.49-128.35H2031.29L2190.47,552,2031.29,772.84h133.35l92.51-128.36,92.5,128.36H2483L2323.85,552Z"/></g></g></svg>""".encode(
            "utf-8"
        )
    ).decode("utf-8")


app_state = {}
css = None
logo = None


def html_base(inner: str):
    return (
        f"""
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aubex OTS</title>
    <style>{css}</style>
</head>
<body>
    <div class="logo"><a href="/"><img src="data:image/svg+xml;base64,{logo}" alt="aubex logo"></a></div>
    <div id="content">{inner}</div>
    <div id="footer">
        <p>&copy; Copyright 2024 by <a href="https://aubex.de/">aubex</a>.
            Single file app available here: <a href="https://github.com/aubex/ots">OTS</a></p>
    </div>
</body>
</html>
"""
    ).strip()


def html_index():
    return html_base(
        """
<h1>OpenSource one time secret (OTS) sharing tool by aubex, Hockenheim.</h1>
<p>Dies ist ein extrem simples and kleines tool zum sicheren Austausch von Geheimnissen wie Passwörtern, z.B. während eines Meetings.</p>
<form action="/new/" class="secret-form" method="post">
    <div>
        <label for="secret">Neues Geheimnis:</label>
        <input type="text" name="secret" id="secret" required="">
    </div>
    <div id="submit">
        <input type="submit" value="Teilen!" />
    </div>
</form>
""".strip()
    )


def html_share(share_token, headers: Dict):
    return html_base(
        f"""
<h1>Ein neues one time secret (OTS) ist bereit.</h1>
<p>Teile den folgenden Link ohne ihn selbst zu öffnen.</p>
<div class="secret-form" id="secret-link">{headers.get('host')}/{share_token}</div>
""".strip()
    )


def html_preview(share_token):
    return html_base(
        f"""
<p>Der erste der auf den folgenden Link klickt, empfängt das OTS und es ist verschwunden.</p>
<a class="button" href="/receive/{share_token}">Zeig es mir!</a>
""".strip()
    )


def html_receive(secret=None):
    if secret is not None:
        return html_base(f"""
<h1>Hier ist dein one time secret (OTS).</h1>
<div class="secret-form" id="secret"></div>
<script>document.getElementById("secret").innerText={json.dumps(secret)}</script>
""")
    else:
        return html_base("<h1>Hier ist kein one time secret (OTS).</h1>")


async def handle_request(method, path, headers, body):
    # This function takes an HTTP method (GET, POST), a path (like "/new"),
    # request headers, and the request body.
    # It returns a suitable HTTP response depending on what the client asked for.

    # If the user visits the homepage ("/") with a GET request, show an index page.
    if method == "GET" and path == "/":
        return response_200(html_index())

    # If the user sends data to "/new" with a POST request, they're trying to store a secret.
    # We parse the submitted data, generate a token (like a "share link"),
    # store it in 'app_state', then redirect them to a page where they can share it.
    if method == "POST" and path.startswith("/new"):
        # Extract form data from the body.
        form_data = parse_qs(body.decode("utf-8"))
        secret = form_data.get("secret", [None])[0]

        # If there's a secret, create a share token and store it.
        if secret:
            share_token = token_urlsafe(6)
            app_state[share_token] = secret
            return response_redirect(f"/share/{share_token}")

        # If no secret was provided, send them back to the homepage.
        return response_redirect("/")

    # If someone visits "/share/XYZ" (a GET request), we show a page where they can receive the secret.
    if method == "GET" and path.startswith("/share/"):
        share_token = path.split("/")[-1]
        return response_200(html_share(share_token, headers))

    # If someone visits "/receive/XYZ" (a GET request), we hand over the secret once and remove it.
    if method == "GET" and path.startswith("/receive/"):
        share_token = path.split("/")[-1]
        secret = app_state.pop(share_token, None)
        return response_200(html_receive(secret))

    # Any other GET request that starts with "/", we treat as a preview of that token's secret.
    # For example, "/XYZ" tries to preview the token XYZ.
    if method == "GET" and path.startswith("/"):
        share_token = path.split("/")[-1]
        return response_200(html_preview(share_token))

    # If none of the above matched, return a "404 Not Found" response.
    return response_404()


def response_200(content):
    return (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(content.encode('utf-8'))}\r\n"
        "\r\n"
        f"{content}"
    ).encode("utf-8")


def response_404():
    content = "<h1>Not Found</h1>"
    return (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(content.encode('utf-8'))}\r\n"
        "\r\n"
        f"{content}"
    ).encode("utf-8")


def response_redirect(location):
    return (
        "HTTP/1.1 303 See Other\r\n"
        f"Location: {location}\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    ).encode("utf-8")


async def handle_client(reader, writer):
    # Be aware we're digging a little deeper here in regards to programming in general and web protocols.
    # This function directly handles the low-level details of communicating with a client over a network connection.
    # It reads the raw HTTP request line by line, extracts the method, path, headers, and body, then calls our main
    # request handler to generate a response. After that, it sends the response back and closes the connection.
    ###############################
    # The first line of an HTTP request typically looks like: "GET / HTTP/1.1"
    # We'll read this line to determine what the client wants.
    request_line = await reader.readline()

    # If there's no request line (like if the client disconnected), we close the connection.
    if not request_line:
        writer.close()
        await writer.wait_closed()
        return

    # Convert the raw bytes into text and remove trailing spaces.
    request_line = request_line.decode("utf-8").strip()
    parts = request_line.split()

    # If we don't have enough parts here (method, path, HTTP version),
    # the request isn't valid. We return a 404 response.
    if len(parts) < 3:
        writer.write(response_404())
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        return

    # Extract the HTTP method (like GET or POST), and the full path.
    # We're ignoring the HTTP version since we assume HTTP/1.1.
    method, full_path, _ = parts

    # We'll store headers in a dictionary for easy lookup.
    headers = {}
    content_length = 0

    # Now we read all the header lines until we hit a blank line "\r\n",
    # which signals the end of the headers section.
    while True:
        line = await reader.readline()
        # If we get no data or just a blank line, we're done reading headers.
        if not line or line == b"\r\n":
            break

        # Decode the header line and split into key and value.
        line_decoded = line.decode("utf-8").strip()
        key, val = line_decoded.split(":", 1)
        key = key.strip().lower()
        val = val.strip()

        headers[key] = val

        # If the Content-Length header exists, record how many bytes we should read from the body.
        if key == "content-length":
            content_length = int(val)

    # If this is a POST request and we have a Content-Length, we read exactly that many bytes
    # from the client to get the request body.
    body = b""
    if method == "POST" and content_length > 0:
        body = await reader.readexactly(content_length)

    # We now pass the method, path, headers, and body to our high-level request handler,
    # which knows how to craft a suitable response.
    response = await handle_request(method, full_path, headers, body)

    # Send the response back to the client.
    writer.write(response)
    await writer.drain()

    # Finally, close the connection since we handled this request.
    writer.close()
    await writer.wait_closed()


async def main(host="0.0.0.0", port=8000):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"Listening on {addr}")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    css = get_css()
    logo = get_logo()
    asyncio.run(main())
