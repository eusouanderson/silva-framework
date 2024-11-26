import asyncio
from silva.core.server import SilvaServer
from silva.router.router import SilvaRouter

class SilvaFramework:
    def __init__(self):
        self.server = SilvaServer(router=SilvaRouter())  
        self.router = self.server.router  

    def route(self, path: str):
        def wrapper(func):
            self.router.add_route(path, func)  
            return func
        return wrapper
    
    def run(self, host='127.0.0.1', port=8000):
        self.server.run(host, port)  

if __name__ == '__main__':
    app = SilvaFramework()

    @app.route("/example")
    async def example_route():
        return "Hello, World!"
    
    @app.route("/example2")
    async def example_route2():
        return "HSDAF "
    
    app.run(host='127.0.0.1', port=8000)
