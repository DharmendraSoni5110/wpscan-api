from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get("url")
    token = data.get("token")
    scan_type = data.get("type", "full")

    if not url or not token:
        return jsonify({"error": "url and token are required"}), 400

    command = ["wpscan", "--url", url, "--api-token", token, "--format", "json"]

    if scan_type == "plugins":
        command += ["--enumerate", "vp"]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=300)
        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
