from core.servers.centralserver import Server
from core.servers.userserviceserver import UserService
from http.server import BaseHTTPRequestHandler,HTTPServer


server = HTTPServer(("localhost", 3000),UserService)
print("Server running at http://localhost:8080/")
server.serve_forever()