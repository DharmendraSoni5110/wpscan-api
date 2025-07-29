from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")
    scan_type = data.get("type", "all")
    token = data.get("token")

    if not url or not token:
        return jsonify({"error": "Missing required parameters"}), 400

    # Fake command for now — replace with your actual WPScan command if needed
    output = f"Scanning {url} with scan type: {scan_type}"

    return jsonify({
        "target": url,
        "type": scan_type,
        "result": output,
        "token": token
    })

@app.route("/", methods=["GET"])
def index():
    return "WPScan API is live", 200

