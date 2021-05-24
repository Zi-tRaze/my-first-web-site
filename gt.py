from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
	return "<p>Welcome to Generation Today<br><b>Home:<br>About Us:<br>Products:<br>Services:<br>Contact Us:</b></p>"

@app.route("/about")
def about():
	return "<b>About</b>"

@app.route("/home")
def home():
	return "<b>Home</b>"	

@app.route("/contact")
def contact():
	return "<b>Contact Us</b>"

@app.route("/products")
def products():
	return "<b>Products</b>"

@app.route("/services")
def services():
	return "<b>Services</b>"

