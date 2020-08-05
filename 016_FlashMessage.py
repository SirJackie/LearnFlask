from flask import Flask, render_template, flash, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string he he"

@app.route("/")
def index():
    return render_template("016_FlashMessage.html")

@app.route("/createMsg")
def createMsg():
    if session.get("FLASH_COUNT") is None:
        session["FLASH_COUNT"] = 1
    else:
        session["FLASH_COUNT"] += 1

    flash("Flash Message %d" % session["FLASH_COUNT"])

    return "<h1>Created Flash Message!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
