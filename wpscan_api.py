from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data.get("url")
    api_token = data.get("token")

    if not url or not api_token:
        return jsonify({"error": "Missing URL or token"}), 400

    # Use WPScan's official remote API
    headers = {"Authorization": f"Token token={api_token}"}
    api_url = f"https://wpscan.com/api/v3/targets"

    try:
        resp = requests.post(api_url, json={"url": url}, headers=headers)
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500
