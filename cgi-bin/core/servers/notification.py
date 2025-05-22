from http.server import BaseHTTPRequestHandler,HTTPServer
import urllib.parse

class  Notification(BaseHTTPRequestHandler):
    def do_GET(self):
        return self.path
    
    