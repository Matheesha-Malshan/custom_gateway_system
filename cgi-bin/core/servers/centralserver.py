from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import urllib.request
from router import router 
from plugging.authentication import  Authentication
from plugging.logging import Log
from plugging.ratelimiter import RateLimiter

authenticate=Authentication()
loggers=Log()
ratelimt=RateLimiter()

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        router_path = urllib.parse.urlparse(self.path)
        auth_header = self.headers.get("Authorization")

        @router(router_path.path) 
        def get_router(base_url):
            if base_url:
                request = f"{base_url}{router_path.path}"

                if router_path.query:
                    request += f"?{router_path.query}"

                try:
                    response = urllib.request.urlopen(request)
                    content = response.read()
                    
                    value=authenticate.auth(auth_header)
                    if value==True:
                        return "autherized"
                    else:
                        return "unotherized"
                    loggers.info()
                    ratelimt.is_allowed()

                    self.send_response(200)
                    self.end_headers()                    
                    self.wfile.write(content)

                except Exception as e:
                    self.send_response(502)
                    self.end_headers()
                    self.wfile.write(f"error: {str(e)}".encode())
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"service not found")

       
