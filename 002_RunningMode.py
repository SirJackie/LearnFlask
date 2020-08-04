#
# Debug Mode Provides 2 Useful Features
# 1.Reloader : Reload server when the code changed
# 2.Debugger : Show the error on browser
#

from flask import Flask

# Create a Flask Instance
app = Flask(__name__)

# Create a Route
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

# Simulate an error
@app.route("/error")
def error():
    return 5/0

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port="80",
            threaded=True)
    # Or Use Following Statements inside Terminal:
    # set FLASK_APP=002_RunningMode.py
    # set FLASK_DEBUG=1
    # flask run -h 0.0.0.0 -p 80 --with-threads
