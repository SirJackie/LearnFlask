from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", username=name)

if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port="80",
            threaded=True)
