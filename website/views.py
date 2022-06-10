from flask import Blueprint, render_template

views = Blueprint('views',__name__)

@views.route ('/')
def home():
    return render_template("index.html")

@views.route ('/simple_clock')
def simple_clock():
    return render_template("simple_clock.html")

@views.route ('/content/')
def content():
    return "<h1>Ini adalah content</h1>"