from http.server import BaseHTTPRequestHandler, HTTPServer


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received GET request\n".encode())

    def do_POST(self):
        self._set_headers()
        content_len = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_len)
        self.wfile.write(
            f"received POST request: ".encode() +
            post_data +
            "\n".encode()
        )
        with open('./db.txt', 'a') as f:
            f.write(f"{post_data.decode()}\n")
        with open('./db.txt') as f:
            lines_str = f"[{', '.join(f.read().splitlines())}]"
            self.wfile.write(
                f"db.txt content: {lines_str}\n".encode()
            )


HTTPServer(('', 8080), HandleRequests).serve_forever()
