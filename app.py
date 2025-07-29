from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return "WPScan API is live!"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")
    scan_type = data.get("type", "plugins")
    token = data.get("token")  # optional, or used if you have WPScan API token

    if not url:
        return jsonify({"error": "Missing target URL"}), 400

    cmd = ["wpscan", "--url", url]

    if scan_type == "plugins":
        cmd += ["--enumerate", "vp"]
    elif scan_type == "themes":
        cmd += ["--enumerate", "vt"]
    elif scan_type == "users":
        cmd += ["--enumerate", "u"]

    if token:
        cmd += ["--api-token", token]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        return jsonify({
            "target": url,
            "output": result.stdout,
            "errors": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
