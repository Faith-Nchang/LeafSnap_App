from flask import Blueprint, render_template, request, current_app
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
        file = request.files.get("leaf_image")
        if file:
            # Save the file to a specific directory
            if file and file.filename:
                upload_folder = os.path.join(current_app.root_path, 'static', 'uploads')
                os.makedirs(upload_folder, exist_ok=True)
                file_path = os.path.join(upload_folder, file.filename)
                file.save(file_path)

            # Process the uploaded file (e.g., save it, analyze it, etc.)
            return render_template("upload.html", alert_message="Success!", file=file)
        else:
            return render_template("upload.html", alert_message="Error!")
    return render_template("upload.html")
