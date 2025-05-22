from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib.parse

class  UserService(BaseHTTPRequestHandler):
    def do_GET(self):
        return self.path
        
          