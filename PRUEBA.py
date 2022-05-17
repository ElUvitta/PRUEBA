from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

@app.route("/")
def index():
	FECHA = now.strftime("%d/%b/%Y")
	time = FECHA
	hora = now.strftime("%H:%M")
	return render_template("index.html", time=time, hora=hora)

@app.route("/comando")
def comando():
	return render_template("comando.html")

@app.route("/xd")
def xd():
	return render_template("xd.html")

# HACER QUE SE EJECUTE SIN "flask run"
if __name__ == "__main__":
	app.run(debug=True)