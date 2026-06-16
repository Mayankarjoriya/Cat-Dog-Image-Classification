# 🐾 Cat vs Dog CNN Classifier

A simple and efficient image classification application that distinguishes between cats and dogs. The project features a deep learning **CNN model** served via a high-performance **FastAPI** backend and wrapped in an intuitive, interactive **Streamlit** frontend web interface.

---

## 🚀 Features

* **FastAPI Backend**: Provides a robust, asynchronous REST API endpoint (`/predict`) for lightning-fast model inference.
* **Streamlit Frontend**: A clean, split-screen UI allowing users to easily upload images and view real-time confidence metrics.
* **Robust Image Preprocessing**: Automatically handles multiple image formats (including Grayscale and RGBA/PNG with transparency) using OpenCV and Pillow, scaling them properly to the model's required `128x128` input shape.
* **Note** : For Image Processing Do not scale image ( by 255.0) because model has a layer for that purpose
* **Modern Python Tooling**: Configurations are fully managed using standard `pyproject.toml` configurations.

---

## 🛠️ Project Structure

```text
├── main.py            # FastAPI backend server & prediction logic
├── frontend.py        # Streamlit web application interface
├── test.py            # Standalone local script for model verification
├── pyproject.toml     # Project metadata and dependencies management
└── image_CNN.keras    # Pre-trained CNN Keras model file (ensure this is in the root)
