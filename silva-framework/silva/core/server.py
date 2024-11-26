import asyncio
import websockets
from silva.router.router import SilvaRouter

class SilvaServer:
    
    def __init__(self, router=None):
        self.router = router if router else SilvaRouter()

    async def handle_request(self, websocket, path='/example'):
        
        route_handler = self.router.get(path)
        if route_handler:
            response = await route_handler()  
            await websocket.send(response)
        else:
            await websocket.send("404 Not Found")  

    def run(self, host='127.0.0.1', port=8000):
        asyncio.run(self._start_server(host, port))

    async def _start_server(self, host, port):
        
        start_server = websockets.serve(self.handle_request, host, port)
        server = await start_server
        print(f'Server running on {host}:{port}')
        await server.wait_closed()
