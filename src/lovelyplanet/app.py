"""Flask web application with intentionally vulnerable patterns for Endor Labs scanning."""

import os

import yaml
from flask import Flask, jsonify, render_template_string, request

from lovelyplanet.utils import encrypt_data, fetch_url

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "super-secret-key-do-not-use-in-prod")


@app.route("/")
def index():
    return jsonify({"status": "ok", "version": "0.1.0"})


@app.route("/greet/<name>")
def greet(name):
    """SSTI risk: user input directly in template string."""
    template = f"<h1>Hello, {name}!</h1>"
    return render_template_string(template)


@app.route("/parse-yaml", methods=["POST"])
def parse_yaml():
    """Uses yaml.load with FullLoader (CVE-2020-14343 pattern)."""
    content = request.get_data(as_text=True)
    data = yaml.load(content, Loader=yaml.FullLoader)
    return jsonify(data)


@app.route("/fetch")
def fetch():
    """Fetch a URL via requests - potential SSRF."""
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "url parameter required"}), 400
    result = fetch_url(url)
    return jsonify({"content": result})


@app.route("/encrypt", methods=["POST"])
def encrypt():
    """Encrypt user-provided data using cryptography."""
    plaintext = request.get_data(as_text=True)
    token = encrypt_data(plaintext)
    return jsonify({"encrypted": token.decode()})


def create_app():
    return app


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
