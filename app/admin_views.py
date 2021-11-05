from flask.templating import render_template
from app import app
from flask import template_rendered

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/admin/profile")
def admin_profile():
    return "your profil"


@app.route("/admin/forum")
def admin_forum():
    return "forum section"

    
@app.route("/admin/webshop")
def admin_webshop():
    return "admin webshop"


@app.route("/admin/cards")
def admin_cards():
    return "cards section"


@app.route("/admin/flashcards")
def admin_flashcards():
    return "flashcards section"


@app.route("/admin/news")
def admin_news():
    return "admin news"