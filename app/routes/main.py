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
            preds = predict(file_path)
            # an error occurred during prediction

            if preds[1] != 200:
                return render_template("upload.html", prediction_error="an error occurred during prediction", file=file)
            else:
                # return prediction
                return render_template("upload.html", alert_message="Success!", file=file, predictions=preds[0])
        else:
            return render_template("upload.html", alert_message="Error!")
    return render_template("upload.html")


def predict(file_path):
    """
    Predict the species of the uploaded leaf image.
    """
    if not file_path:
        return {"error": "No file path provided."}, 400

    try:
        img_array = load_and_preprocess_image(file_path)
        print(model.input_shape)
        preds = model.predict(img_array)
        print("Predictions:", preds)

        predicted_class = np.argmax(preds, axis=1)

        index = predicted_class[0]

        return CLASS_NAMES[index], 200

    except Exception:
        
        return {"error": "Prediction failed."}, 500
       

def load_and_preprocess_image(img_path, target_size=(224, 224)):
    # Load the image
    img = image.load_img(img_path, target_size=target_size)
    # Convert to array
    img_array = image.img_to_array(img)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Scale pixel values if your model was trained on normalized images
    img_array /= 255.0
    return img_array
