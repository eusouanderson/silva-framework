import asyncio
import websockets

async def test_websocket():
    async with websockets.connect('ws://127.0.0.1:8000/example2') as websocket:
        response = await websocket.recv()
        print(response)

# Executa a função de teste
asyncio.run(test_websocket())
