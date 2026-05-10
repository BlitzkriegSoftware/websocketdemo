import falcon
import jinja2
import falcon.asgi
import uvicorn

with open("index.html", 'r') as file:
    html = file.read()

class ChatResource:
    async def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        template = jinja2.Template(html)
        resp.body = template.render()

    async def on_websocket(self, req, websocket):
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message: {data}")

app = falcon.asgi.App()
chat = ChatResource()
app.add_route('/chat', chat)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)