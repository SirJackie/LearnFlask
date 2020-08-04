from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("009_ChildTemplate.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
