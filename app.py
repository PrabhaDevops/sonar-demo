
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "message": "sonar-demo is running",
            "status": "success"
        }

        body = json.dumps(response).encode()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

if __name__ == "__main__":
    print("Starting sonar-demo on port 8000")
    HTTPServer(("0.0.0.0", 8000), AppHandler).serve_forever()

