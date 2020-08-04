from flask import Flask, render_template

app = Flask(__name__)


class ObjectClass:
    def method(self):
        return "Return Value From object.method()"


@app.route("/")
def index():
    return render_template("004_ComplexTemplate.html",
                           list=[0, 1, 2, 3, 4],
                           i=3,
                           dict={"key": "value"},
                           object=ObjectClass(),
                           sentence="this is a sentence.",
                           HTMLString=" <h3>Hello World</h3> ")


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
