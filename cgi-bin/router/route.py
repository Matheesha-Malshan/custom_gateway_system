def router(path):
    def decorator(func):
        def wrapper():
            routes = {
                "/users": "http://localhost:3001",
                "/payment": "http://localhost:3002",
                "/notification": "http://localhost:3003"
            }
            base_url = routes.get(path)
            return func(base_url)
        return wrapper
    return decorator
