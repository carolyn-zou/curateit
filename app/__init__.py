# app/__init__.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    """
    Health-check endpoint.
    Recruiters (and Render) can hit `/` to verify the API is live.
    """
    return jsonify(message="CurateIt API is running"), 200