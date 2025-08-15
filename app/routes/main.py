from flask import Blueprint, render_template, request, redirect, url_for
import os


main = Blueprint('main', __name__)


# home route
@main.route("/")
def index():
    return render_template("index.html")


#upload route
@main.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
       print("File uploaded")
    return render_template("upload.html")
