import time

class RateLimiter:
    def __init__(self):
   
        self.request_log = {}
        self.max_requests = 10
        self.window = 60

    def is_allowed(self, client_key):
        current_time = time.time()

        if client_key not in self.request_log:
            self.request_log[client_key] = []

        # Remove timestamps older than window
        self.request_log[client_key] = [
            timestamp for timestamp in self.request_log[client_key]
            if current_time - timestamp < self.window
        ]

        # Check current count
        if len(self.request_log[client_key]) >= self.max_requests:
            return False  # Too many requests

        # Log this request
        self.request_log[client_key].append(current_time)
        return True  # Request is allowed

                    
