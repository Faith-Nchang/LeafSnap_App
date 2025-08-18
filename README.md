

# LeafSnap: Plant Leaf Identification App

LeafSnap is a deep learning-based web application that identifies plant species from leaf images. This project leverages a convolutional neural network (CNN) trained on the LeafSnap dataset and exposes a Flask-based interface for predictions.

---

## **Features**

* Identify plant species from uploaded leaf images.
* Simple, user-friendly web interface built with Flask.
* Preprocessing ensures consistent image size and normalization.
* Model trained using transfer learning and CNN architectures for high accuracy.

---

## **Dataset**

* The project uses the **LeafSnap dataset** from kaggle(fields and lab images).
* **Source:** [LeafSnap Dataset](http://leafsnap.com/dataset/) 
* Contains over **10,000 images** across **185 species**.

> **Note:** The dataset is included for testing purposes locally but is **not pushed to GitHub** to avoid large file sizes. Ensure you have access to the original dataset if reproducing this project.

---

## **Training**

* Preprocessing:

  * Resize images to `(224, 224)`.
  * Normalize pixel values (`/255.0`).
* Model architecture: CNN with convolutional layers, max pooling, and dense layers for classification.
* Optimizer: Adam, loss: categorical cross-entropy.
* Validation split: 20%.
* Early stopping used to prevent overfitting.

---


## **Project Structure**

```
leafsnap_app/
│
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── main.py       # Flask route handlers
│   │   └── __init__.py
│   ├── models/
│   │   └── model.keras   # Trained CNN model
│   ├── static/
│   │   └── css/
│   │       └── home.css
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── upload.html
│
├── data/                 # Dataset folder (ignored in Git)
├── notebooks/            # Jupyter notebooks for EDA and training
├── run.py                # Entry point to start Flask app
├── requirements.txt      # Python dependencies
└── README.md
```

---

## **Setup**

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd leafsnap_app
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. Ensure the LeafSnap dataset is downloaded locally in `data/`.

4. Run the Flask app:

   ```bash
   python run.py
   ```

5. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to use the app.

---

## **Usage**

1. Navigate to the homepage and click **Get Started**.
2. Upload a leaf image (lab or field).
3. The app will predict the species using the trained CNN model.


---

## **Credits**

* LeafSnap Dataset: Kaggle
* Flask Framework: [Flask](https://flask.palletsprojects.com/)
* TensorFlow/Keras: [TensorFlow](https://www.tensorflow.org/)

---

## **License**

This project is for educational purposes. The dataset is used in accordance with its terms of use.

