from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("011_UrlFor.html")

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, %s</h1>" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
