from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import tensorflow as tf
# Disable GPU to avoid CUDA initialization errors
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.set_visible_devices([], 'GPU')
    except Exception as e:
        # Fallback: ignore if setting fails
        pass

import cv2

import builtins
builtins.tf = tf  




app = FastAPI()
model = None

def load_model():
    global model
    # Ensure TensorFlow runs on CPU only
    try:
        tf.config.set_visible_devices([], 'GPU')
    except Exception:
        pass
    if model is None:
        model = tf.keras.models.load_model("image_CNN.keras", safe_mode=False,custom_objects={'tf':tf})
        
    return model




def preprocess_image(pil_image: Image.Image):
    # Convert PIL Image to a NumPy array (RGB)
    np_image = np.array(pil_image)

    # Handle images with alpha channel or grayscale
    if np_image.ndim == 2:
        np_image = cv2.cvtColor(np_image, cv2.COLOR_GRAY2RGB)
    elif np_image.shape[2] == 4:
        np_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2RGB)

    # Resize and normalize
    img_resized = cv2.resize(np_image, (128, 128))
    img_normalized = img_resized.astype('float32') 

    processed_image = np.expand_dims(img_normalized, axis=0)
    return processed_image

def predicted_label(prob):
    if prob > 0.5:
        return "Dog", prob * 100
    else:
        return "Cat", (1 - prob) * 100

# #############################################
# Endpoints
# #############################################

@app.get("/")
def read_root():
    return {"message": "Cat vs Dog API Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        processed_image = preprocess_image(image)

        model = load_model()
        prediction = model.predict(processed_image, verbose=0)

        if hasattr(prediction, "tolist"):
            prediction = prediction.tolist()

        label, confidence = predicted_label(prediction[0][0])

        return JSONResponse(content={"label": label, "confidence": confidence})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})