from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/about")
def about():
    return render_template("public/about.html")


@app.route("/projects")
def projects():
    return render_template("public/projects.html")


@app.route("/cards")
def cards():
    return render_template("public/cards.html")


@app.route("/news")
def news():
    return render_template("public/news.html")


@app.route("/contact")
def contact():
    return render_template("public/contact.html")