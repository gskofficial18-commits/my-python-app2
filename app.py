from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now().strftime("%d %b %Y, %H:%M:%S")
    return f"""
    <html>
      <head><title>My Python App</title></head>
      <body style="font-family:sans-serif;text-align:center;margin-top:80px">
        <h1>Hello from AWS EC2 🚀</h1>
        <p>My Python app is running and deployed through GitHub.</p>
        <p>Server time: {now}</p>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
