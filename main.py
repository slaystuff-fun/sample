from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello from slaystuff.fun!</h1><p>Edit main.py to build your project.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
