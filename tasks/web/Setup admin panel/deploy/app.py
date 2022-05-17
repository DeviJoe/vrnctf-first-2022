from flask import Flask

app = Flask(__name__)


@app.route("/admin")
def admin():
    return "vrnctf{5dm3n_p3nel6}"


@app.route("/")
def hello():
    return "Find me!"


if __name__ == "__main__":
    app.run()
