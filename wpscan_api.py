from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")
    scan_type = data.get("type")
    token = data.get("token")

    if not url or not scan_type or not token:
        return jsonify({"error": "Missing required fields"}), 400

    # Run the WPScan command (ensure wpscan is installed on your machine or container)
    try:
        result = subprocess.run(
            ["wpscan", "--url", url, f"--{scan_type}", "--api-token", token],
            capture_output=True, text=True, check=True
        )
        return jsonify({"output": result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.stderr}), 500
