from flask import Flask

# Create a Flask Instance
app = Flask(__name__)

# Use @app.route() Decorator to Create a Route
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

# Or you can use app.add_url_rule() to Create a Route
def page():
    return "<h1>This page was added by app.add_url_rule() Function.</h1>"
app.add_url_rule("/page", "page", page)

# Create a Changeable Route
@app.route("/user/<name>")
def user(name):
    return "<h1>Username: %s</h1>" % name

if __name__ == "__main__":
    app.run()
