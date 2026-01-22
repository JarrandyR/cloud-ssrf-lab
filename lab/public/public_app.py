from flask import Flask, request, Response
import requests
import socket
import ipaddress

app = Flask(__name__)

def is_blocked_destination(url):
    try:
        hostname = url.split("//")[-1].split("/")[0]
        ip = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(ip)

        return (
            ip_obj.is_loopback or
            ip_obj.is_private or
            ip_obj.is_link_local
        )
    except Exception:
        return True

@app.get("/")
def index():
    return """
    <h2>SSRF Lab - Public App</h2>
    <p>Example:</p>
    <code>/fetch?url=http://example.com</code><br>
    <code>/fetch?url=http://127.0.0.1:5001/internal/secret</code>
    """

@app.get("/fetch")
def fetch():
    url = request.args.get("url")
    if not url:
        return Response("Missing 'url' parameter", status=400)

    if is_blocked_destination(url):
        return Response("Blocked by SSRF protection", status=403)

    try:
        r = requests.get(url, timeout=3)
        return Response(r.text, status=200)
    except Exception as e:
        return Response(f"Error: {e}", status=502)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
