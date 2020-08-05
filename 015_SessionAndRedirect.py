from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string ha ha ha Blah Blah Blah"
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField("用户名", validators=[DataRequired()])
    password = PasswordField("密码", validators=[DataRequired()])
    submit = SubmitField("提交")

@app.route("/", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        session["username"] = form.username.data
        session["password"] = form.password.data
        return redirect(url_for("index"))
    return render_template("015_SessionAndRedirect.html",
                            form=form,
                            username=session.get("username"),
                            password=session.get("password"))

@app.route("/logout")
def logout():
    session["username"] = None
    session["password"] = None
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
