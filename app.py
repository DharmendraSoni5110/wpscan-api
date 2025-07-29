from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "WPScan API is running."

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url")
    scan_type = data.get("type", "all")
    token = data.get("token")

    if not url or not token:
        return jsonify({"error": "Missing 'url' or 'token'"}), 400

    cmd = ["wpscan", "--url", url, "--api-token", token]
    
    if scan_type == "plugins":
        cmd += ["--enumerate", "vp"]
    elif scan_type == "themes":
        cmd += ["--enumerate", "vt"]
    elif scan_type == "users":
        cmd += ["--enumerate", "u"]
    elif scan_type == "all":
        cmd += ["--enumerate", "vp,vt,u"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return jsonify({
            "target": url,
            "type": scan_type,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
