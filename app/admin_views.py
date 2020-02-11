from app import app

@app.route("/admin")
def admin():
	return "<h1>ADDmin<h1>"

@app.route("/hoi")
def hoi():
	return "<h2 style = 'color: red'>no<h2>"

@app.route("/chin")
def chin():
	return "<h style = 'color: blue' >hoi chinmoy<h>"