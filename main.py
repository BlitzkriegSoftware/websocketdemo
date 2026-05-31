import os

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn


# Manage multiple ws connections
class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

# Read in PORT env var
port = int(os.environ.get("PORT", 8000))

app = FastAPI()

# Read in chat app page
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read()
    html = html.replace("##PORT##", str(port))


# Serve chat app page
@app.get("/")
async def get():
    return HTMLResponse(html)


# Serve websocket chat
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Someone said: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")


if __name__ == "__main__":
    print("Port: ", port)
    uvicorn.run(
        "main:app",  # Replace 'main' with your actual file name
        host="127.0.0.1",  # Use "0.0.0.0" to accept external requests
        port=port,  # Set your custom port number here
        reload=True,  # Enables auto-reload during development
    )
