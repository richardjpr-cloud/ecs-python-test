from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = {
            "status": "success",
            "message": "Python app is running on AWS ECS!",
            "hostname": os.uname().nodename,
        }

        body = str(message).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(format % args)


port = int(os.environ.get("PORT", 8000))

server = HTTPServer(("0.0.0.0", port), Handler)

print(f"Server running on port {port}")

server.serve_forever()
