from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/cart")
def cart():
    return "<p>Meus produtos!</p>"

@app.route('/user/')
@app.route('/user/<username>')
def profile(username=None):
    return render_template('profile.html', username=username)