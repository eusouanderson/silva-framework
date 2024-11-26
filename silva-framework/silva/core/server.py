import asyncio
import websockets
from router import router


class SilvaServer:
    def __init__(self, router=router()):
        self.router = router

    async def handle_request(self, websocket, path):
        route_handler = self.router.get(path)
        if route_handler:
            response = await route_handler()        
            await websocket.send(response)
        else:
            await websocket.send("404 Not Found")

    def run(self, host='127.0.0.1', port=8000):
        start_server = websockets.serve(self.handle_request, host, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        print(f'Server running on {host}:{port}')
        asyncio.get_event_loop().run_forever()

