from app import app
from flask import render_template

@app.route("/")
def index():
	return render_template("test.html")

@app.route("/a")
def a():
	return "<h2 style = 'color: red'>about<h2>"