from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        message = "Bonjour depuis mon conteneur Docker ! 🐳"
        self.wfile.write(message.encode("utf-8"))

print("Serveur démarré sur le port 8000...")
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
