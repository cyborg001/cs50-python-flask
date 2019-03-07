from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!!!S"

@app.route('/<string:name>')
def name(name):
    return f"Hello mr {name}"

@app.route('/rend/<string:name>')
def rend(name):
    return render_template("index.html",name=name)
