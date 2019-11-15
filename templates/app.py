from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data')
def data():
    return render_template("data.html")


@app.route('/mango')
def mango():
    return render_template("mango.html")


@app.route('/coala')
def coala():
    return render_template("coala.html")


if __name__ == '__main__':
    app.run()