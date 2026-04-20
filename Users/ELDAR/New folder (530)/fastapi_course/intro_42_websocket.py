from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI()


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Eldar Chat</title>
        <style>
            body { font-family: sans-serif; margin: 20px; }
            #messages { list-style-type: none; padding: 0; }
            li { background: #f4f4f4; margin: 5px; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>FastAPI Canlı Çat 💬</h1>
        <input type="text" id="messageText" placeholder="Mesaj yaz..." autocomplete="off"/>
        <button onclick="sendMessage(event)">Göndər</button>
        <ul id='messages'></ul>
        
        <script>
            // WebSocket bağlantısını qururuq
            var ws = new WebSocket("ws://localhost:8007/ws");

            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };

            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""



@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Senin mesajin: {data}")
    except WebSocketDisconnect:
        print("Istifadeci catdan cixdi.")