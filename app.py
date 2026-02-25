from flask import Flask, jsonify, request
from datetime import datetime
import requests

# Initialize the Flask application
# static_folder='.' tells Flask to serve static files from the current directory
# static_url_path='' means the files will be served at the root URL (e.g., /style.css)
app = Flask(__name__, static_folder='.', static_url_path='')

def get_location(ip):
    """Fetch geolocation data for an IP address."""
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=3)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return {}


def send_visitor_info(ip, date, page, referrer, user_agent, location):
    webhook_url = "https://discord.com/api/webhooks/1476256421438951526/1XbFzQdfe3YZTQN_MyA8Uc41JSBOVsgG7p747qa7i9AY66EzPbaUfxBXv0pdfwY9fLp3"

    loc_str = "Unknown"
    if location:
        city = location.get("city", "")
        region = location.get("regionName", "")
        country = location.get("country", "")
        zip_code = location.get("zip", "")
        lat = location.get("lat", "")
        lon = location.get("lon", "")
        isp = location.get("isp", "")
        org = location.get("org", "")
        timezone = location.get("timezone", "")
        loc_str = f"{city}, {region}, {country}"

    fields = [
        {"name": "🌐 IP", "value": f"`{ip}`", "inline": True},
        {"name": "🕐 Timestamp", "value": date, "inline": True},
        {"name": "📄 Page", "value": page or "/", "inline": True},
        {"name": "🔗 Referrer", "value": referrer or "Direct", "inline": True},
        {"name": "📍 Location", "value": loc_str, "inline": False},
    ]

    if location:
        fields.extend([
            {"name": "📮 Zip", "value": str(zip_code), "inline": True},
            {"name": "🗺️ Coordinates", "value": f"{lat}, {lon}", "inline": True},
            {"name": "🕰️ Timezone", "value": timezone, "inline": True},
            {"name": "📡 ISP", "value": isp, "inline": True},
            {"name": "🏢 Org", "value": org, "inline": True},
        ])

    fields.append({"name": "💻 User Agent", "value": f"```{user_agent}```", "inline": False})

    data = {
        "embeds": [
            {
                "title": "🌿 New Visitor",
                "color": 0x88a550,
                "fields": fields,
                "timestamp": datetime.utcnow().isoformat()
            }
        ]
    }
    try:
        requests.post(webhook_url, json=data)
    except Exception:
        pass


@app.route('/')
def index():
    """Serve the main index.html file."""
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    page = request.path
    referrer = request.referrer
    user_agent = request.headers.get("User-Agent", "Unknown")
    location = get_location(ip)
    send_visitor_info(ip, date, page, referrer, user_agent, location)
    return app.send_static_file('index.html')


@app.route('/api/hello')
def hello():
    """Example API endpoint."""
    return jsonify(message="Hello from the Flask backend server!")


if __name__ == '__main__':
    # Run the server on port 3000
    app.run(port=3000, debug=True)

