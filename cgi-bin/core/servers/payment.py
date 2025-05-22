from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib.parse

class Payment(BaseHTTPRequestHandler):
    def do_GET(self):
        return self.path