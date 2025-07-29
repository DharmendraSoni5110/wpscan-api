from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    url = data.get("url")
    scan_type = data.get("type")
    token = data.get("token")

    if not url or not scan_type or not token:
        return jsonify({"error": "Missing parameters"}), 400

    # Dummy response for demonstration
    return jsonify({
        "status": "success",
        "message": f"Scanned {url} for {scan_type} using token {token[:5]}..."
    })