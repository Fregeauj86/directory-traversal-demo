from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath("files")

@app.route("/")
def index():
    return '''
    <h2>File Viewer</h2>
    <p>Try accessing: <code>?file=about.txt</code></p>
    '''

@app.route("/view")
def view_file():
    filename = request.args.get("file", "")
    try:
        # ❗ This is intentionally vulnerable to directory traversal
        file_path = os.path.join(BASE_DIR, filename)
        return send_from_directory(BASE_DIR, filename)
    except Exception as e:
        return f"<p>Error: {e}</p>"

if __name__ == "__main__":
    app.run(debug=True)