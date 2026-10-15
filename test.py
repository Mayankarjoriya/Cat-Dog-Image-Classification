import numpy as np
import os
import tensorflow as tf
import cv2


import builtins
builtins.tf = tf  


os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

print("Available devices:", tf.config.list_physical_devices())


try:
    # 2. Load the model (Replace with your exact filename if different)
    model = tf.keras.models.load_model("image_CNN.keras",
                                     safe_mode=False,
                                     custom_objects={'tf':tf},
                                     compile=False)

    # print("✅ Model loaded successfully!", flush=True)
    print(model.summary())

    sample_image = cv2.imread('images/dog.png')
    sample_image = cv2.cvtColor(sample_image, cv2.COLOR_BGR2RGB)

    img_resized = cv2.resize(sample_image, (128,128))

    img_normalized = img_resized.astype('float32')

    processed_image = np.expand_dims(img_normalized,axis=0)

    
    # 3. Create dummy data (Replace this with your actual image processing)
    # Model expects (batch_size, 128, 128, 3) for RGB images:
    sample_input = np.random.rand(1, 128, 128, 3).astype(np.float32)  # Example shape for a grayscale image
    
    # 4. Generate prediction
    predictions = model.predict(processed_image, verbose=0) # verbose=0 completely hides the loading bar
    prob = predictions[0][0]

    if prob > 0.5:
        predicted_label ="Dog"
        confidence = prob
    else:
        predicted_label = "Cat"
        confidence = 1- prob

    
    
    # 5. Print results clearly using flush=True
    print("\n================ RESULTS ================", flush=True)
    print(f"Raw Probobility:{prob}")
    print(f"Prediction: {predicted_label}", flush=True)
    print(f"Confidence: {confidence:.2%}", flush=True)

    print("=========================================\n", flush=True)

except Exception as e:
    print(f"❌ An error occurred: {e}", flush=True)
