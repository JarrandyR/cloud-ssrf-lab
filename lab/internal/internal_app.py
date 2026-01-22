from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/internal/health")
def health():
    return jsonify(
        status="ok",
        service="internal-only",
        note="This endpoint should NOT be internet-accessible"
    )

@app.route("/internal/secret")
def secret():
    return jsonify(
        secret="INTERNAL_API_KEY_ABC123",
        impact="If this is reachable via SSRF, the lab worked"
    )

if __name__ == "__main__":
    # Bind ONLY to localhost
    app.run(host="127.0.0.1", port=5001)
