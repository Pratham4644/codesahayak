# Create: run_server.py in C:\Users\bs529\Documents\codesahayak\
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CodeSahayak - SUCCESS! 🎉</title>
    <style>
        body { 
            font-family: Arial; 
            background: linear-gradient(135deg, #667eea, #764ba2);
            margin: 0;
            padding: 40px;
            color: white;
            text-align: center;
        }
        .success-box {
            background: white;
            color: #333;
            padding: 40px;
            border-radius: 15px;
            margin: 20px auto;
            max-width: 500px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 { color: #28a745; font-size: 2.5em; }
        button {
            background: #28a745;
            color: white;
            border: none;
            padding: 15px 30px;
            font-size: 1.2em;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div class="success-box">
        <h1>🎉 SUCCESS!</h1>
        <h2>CodeSahayak is Running!</h2>
        <p>Your AI coding mentor server is now live!</p>
        <button onclick="showMessage()">Test It!</button>
        <div id="message" style="margin-top: 20px;"></div>
    </div>

    <script>
        function showMessage() {
            document.getElementById('message').innerHTML = 
                '<div style="background: #d4edda; color: #155724; padding: 15px; border-radius: 8px;">' +
                '✅ Perfect! Your server is working!<br>' +
                '🎤 Voice Agent: "नमस्कार! मी CodeSahayak आहे"</div>';
        }
    </script>
</body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(HTML)

if __name__ == "__main__":
    print("🎯 ===================================")
    print("🚀 CODE SAHAYAK SERVER STARTING...")
    print("📱 Open: http://localhost:8000")
    print("🛑 Press CTRL+C to stop")
    print("🎯 ===================================")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)