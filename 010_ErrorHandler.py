from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/error")
def error():
    return 5/0

@app.errorhandler(404)
def error404(e):
    return "<h1>404 Not Found, Try to access other pages.</h1>", 404

@app.errorhandler(500)
def error404(e):
    return "<h1>There is an error inside server.</h1>", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=False)
