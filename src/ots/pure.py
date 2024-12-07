import secrets
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

# Store secrets in memory
secrets_store = {}


class SecretServer(BaseHTTPRequestHandler):
    def init_ok_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def init_redirect_response(self, url: str):
        self.send_response(303)
        self.send_header("Location", url)
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/":
            self.init_ok_response()
            self.wfile.write(self.render_index().encode())
        else:
            token = path.split("/")[-1]
            self.init_ok_response()

            if "receive" in path:
                secret = secrets_store.pop(token, None)
                return self.wfile.write(self.render_receive(secret).encode())
            if "share" in path:
                return self.wfile.write(self.render_share(token).encode())
            if "secret" in path:
                return self.wfile.write(self.render_preview(token).encode())

    def do_POST(self):
        if self.path == "/secret/new/":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode()
            token = secrets.token_urlsafe(4)
            secrets_store[token] = parse_qs(post_data)["secret"][0]

            self.init_redirect_response(f"/secret/share/{token}")

    def render_index(self):
        return """
            <p>Share a Secret</p>
            <form action="/secret/new/" method="post">
                <input name="secret" required></input>
                <button type="submit">share</button>
            </form>
            """

    def render_share(self, token):
        preview_url = f"http://{self.headers['Host']}/secret/{token}"
        return f"<p>Share this: <a href='{preview_url}'>{preview_url}</a></p>"

    def render_preview(self, token):
        return f"<p>Someone shared a secret with you: <a href='/secret/receive/{token}'>show me</a></p>"

    def render_receive(self, secret):
        if secret is None:
            return "<p>Secret Not Found</p>"
        return f"<p>{secret}</p>"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Secret Server")
    parser.add_argument(
        "--port", type=int, default=8100, help="Port to run the server on"
    )
    args = parser.parse_args()

    server = HTTPServer(("", args.port), SecretServer)
    print(f"Server running on port {args.port}")
    server.serve_forever()
