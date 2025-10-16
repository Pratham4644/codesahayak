# chat_server.py - EVERYTHING IN ONE FILE
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
import json

app = FastAPI()

# HTML embedded as string
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CodeSahayak Chat</title>
    <style>
        /* All CSS here */
        body { font-family: Arial; background: #f0f0f0; }
        .chat-container { max-width: 800px; margin: 0 auto; }
        /* ... rest of CSS */
    </style>
</head>
<body>
    <div class="chat-container">
        <!-- Chat interface HTML -->
    </div>
    <script>
        // All JavaScript here
        // WebSocket connection, event handlers, etc.
    </script>
</body>
</html>
"""

@app.get("/")
async def home():
    return HTMLResponse(HTML)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # WebSocket handling code
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)