from flask import Blueprint, render_template, request, current_app
import os, json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 
from PIL import Image
import numpy as np

main = Blueprint('main', __name__)





# Load model and class names once at startup using path relative to this file
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODELS_DIR, 'model.keras')
CLASS_NAMES_PATH = os.path.join(MODELS_DIR, 'class_names.json')
print(f"Loading model from: {MODEL_PATH}")
model = load_model(MODEL_PATH)
with open(CLASS_NAMES_PATH, 'r') as f:
    CLASS_NAMES = json.load(f).get('classnames', [])





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
            
            # make a prediction
            preds = model.predict(file_path)
            # an error occurred during prediction

            if preds[1] != 200:
                return render_template("upload.html", prediction_error="an error occurred during prediction", file=file)
            else:
                # return prediction
                return render_template("upload.html", alert_message="Success!", file=file, predictions=preds[0])
        else:
            return render_template("upload.html", alert_message="Error!")
    return render_template("upload.html")

