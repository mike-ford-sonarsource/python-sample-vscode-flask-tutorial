from datetime import datetime
from flask import Flask, render_template, request, jsonify
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.json
    if not data or not isinstance(data, list):
        return jsonify({"error": "Invalid input, expected a list of numbers"}), 400

    try:
        numbers = [float(num) for num in data]
    except ValueError:
        return jsonify({"error": "All elements must be numbers"}), 400

    return jsonify({"sum": sum(numbers)})
