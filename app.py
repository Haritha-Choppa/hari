from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Haritha! 🚀 Flask app is running!"
