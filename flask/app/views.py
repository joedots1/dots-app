from flask import render_template
from app import app 
import os 

@app.route("/")
def index():

    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in Docker"

    return "hello from flask!"

@app.route("/home")
def home():
    return render_template('index.html')