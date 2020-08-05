from flask import Flask, render_template
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
    username = None
    password = None
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        form.username.data = None
        form.password.data = None
    return render_template("014_Flask-WTF.html",
                            form=form,
                            username=username,
                            password=password)

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="80",
            threaded=True,
            debug=True)
