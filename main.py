# coding:utf-8

from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from NameForm import NameForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'f9f7996042dd95e75200ff21aa2c89f68afb309bb8898a5c98f8d6a6c7b9d956'

bootstrap = Bootstrap(app)

@app.route("/", methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return "the server is hang bronsis", 500


if __name__ == "__main__":
    app.run()
