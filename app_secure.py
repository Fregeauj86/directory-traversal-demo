from flask import Flask, request, send_file
import os

app = Flask(__name__)

# Secure base directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../files"))

@app.route("/view")
def view_file():
    filename = request.args.get("file", "")

    # Clean and validate path
    requested_path = os.path.abspath(os.path.join(BASE_DIR, filename))

    if not requested_path.startswith(BASE_DIR):
        return "Access denied: directory traversal attempt blocked", 403

    try:
        return send_file(requested_path)
    except Exception as e:
        return f"Error: {e}", 404

if __name__ == "__main__":
    app.run(debug=True)