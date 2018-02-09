from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/")
def images():
    return render_template('layout.html')

@app.route("/upload")
def upload():
    return render_template('layout.html')
