from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data.get("url")
    scan_type = data.get("type", "full")
    api_token = data.get("token")

    if not all([url, api_token]):
        return jsonify({"error": "Missing URL or API token"}), 400

    cmd = ["wpscan", "--url", url, "--api-token", api_token]

    if scan_type == "plugins":
        cmd += ["--enumerate", "vp"]
    elif scan_type == "themes":
        cmd += ["--enumerate", "vt"]

    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode()
        return jsonify({"output": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode()}), 500

if __name__ == "__main__":
    app.run()
