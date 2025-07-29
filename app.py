from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "WPScan API is live!"

@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    url = data.get("url")
    scan_type = data.get("type", "all")
    token = data.get("token")  # ✅ get the API token

    if not url:
        return jsonify({"error": "Missing 'url' in request"}), 400

    try:
        # ✅ Build base WPScan command
        cmd = [
            "wpscan",
            "--url", url,
            "--no-update",
            "--format", "json",
            "--force",
            "--random-user-agent"
        ]

        if scan_type == "plugins":
            cmd += ["--enumerate", "vp"]
        elif scan_type == "themes":
            cmd += ["--enumerate", "vt"]
        elif scan_type == "users":
            cmd += ["--enumerate", "u"]

        if token:
            cmd += ["--api-token", token]

        # ✅ Run the scan
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Scan timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500
