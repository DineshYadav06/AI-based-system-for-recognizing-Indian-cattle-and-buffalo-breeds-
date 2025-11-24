from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

# Load CNN model
model = tf.keras.models.load_model("cnn_model.h5")

@app.route("/")
def home():
    return {"message": "CNN Model API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "Please upload an image file"}), 400
    
    file = request.files["file"]
    img = Image.open(file.stream).resize((128, 128))  # change to your model size
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    predicted_class = int(np.argmax(prediction))

    return jsonify({
        "predicted_class": predicted_class,
        "confidence": float(np.max(prediction))
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
