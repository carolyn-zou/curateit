# run.py
"""
Entry-point script for local development.
Running `python run.py` boots the Flask dev server.
"""
from app import app

if __name__ == "__main__":
    # debug=True enables hot-reload so you see changes instantly
    app.run(debug=True, host="127.0.0.1", port=5000)