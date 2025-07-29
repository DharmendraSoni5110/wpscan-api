from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "WPScan API is running!"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url")
    scan_type = data.get("type")
    token = data.get("token")

    if not url or not scan_type or not token:
        return jsonify({"error": "Missing required fields"}), 400

    # Simulate WPScan output (replace this with subprocess in production)
    return jsonify({
        "result": f"Scanning {url} with scan type: {scan_type}",
        "target": url,
        "token": token,
        "type": scan_type
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
