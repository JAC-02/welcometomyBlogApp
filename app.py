from flask import Flask, render_template, request, flash

app = Flask(__name__) 
app.secret_key = "manbearpig-MUDMAN88"

@app.route("/hello")
def index():
	flash("Hey, Welcome to My Blog! What's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", Welcome! Glad to have you!")
	return render_template("index.html")
	
