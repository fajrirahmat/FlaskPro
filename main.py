# coding:utf-8

from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return '<h1>Hello %s!</h1>' % name

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Your browser is %s</h1>' % user_agent

if __name__ == "__main__":
    app.run()
