from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)

@app.route("/")
def index():
    return render_template("013_Flask-Moment.html",
                           current_time=datetime.utcnow())

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
