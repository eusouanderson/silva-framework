import asyncio
from server import server
from router import router

class SilvaFramework:
    def __init__(self):
        self.server = server()
        self.router = router()

    def route(self, path: str):
        def wrapper(func):
            self.router.add_route(path, func)
            return func
        return wrapper
    
    def run(self, host='127.0.0.1', port=8000):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.server.run(host, port))

