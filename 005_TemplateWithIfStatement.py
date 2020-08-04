from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("005_TemplateWithIfStatement.html")

@app.route("/user/<name>")
def user(name):
    return render_template("005_TemplateWithIfStatement.html",
                           user=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
