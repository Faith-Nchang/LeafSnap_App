from flask import Blueprint, render_template, request, redirect, url_for
import os


main = Blueprint('main', __name__)


# home route
@main.route("/")
def index():
    return render_template("index.html")

