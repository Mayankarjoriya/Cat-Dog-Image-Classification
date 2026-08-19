# CNN Classifier

## Overview

This repository contains a simple **Cat vs. Dog image classification** service built with **FastAPI** for the backend API and **Streamlit** for a minimal frontend UI. The model is a pre‑trained Keras CNN stored in `image_CNN.keras` and can classify images of cats and dogs with confidence scores.

---

## Project Structure

- `main.py` – FastAPI application exposing `/predict` endpoint.
- `frontend.py` – Streamlit app for uploading images and displaying predictions.
- `image_CNN.keras` – Trained TensorFlow/Keras model.
- `pyproject.toml` – Project metadata and dependencies.
- `README.md` – This documentation.

---

## Prerequisites

- **Python ≥ 3.12** (as specified in `pyproject.toml`).
- `git` (to clone the repository).
- Internet connection for downloading the required Python packages.

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cnn-classifier.git
   cd cnn-classifier
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   The project uses a `pyproject.toml` file. Install the required packages with:
   ```bash
   pip install .
   # Alternatively, you can install directly from the TOML dependencies:
   # pip install fastapi opencv-python pillow python-multipart streamlit uvicorn
   ```

4. **Run the FastAPI backend**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080
   ```
   The API will be available at `http://localhost:8080`.

5. **Run the Streamlit frontend** (in a separate terminal)
   ```bash
   streamlit run frontend.py
   ```
   Open the displayed URL (usually `http://localhost:8501`) in your browser.

---

## Usage

### Via the Streamlit UI

1. Open the Streamlit app URL.
2. Upload a JPG/PNG image of a cat or dog.
3. Click **Predict**.
4. The result (label and confidence) will appear on the right side.

### Direct API call (cURL example)

```bash
curl -X POST "http://localhost:8080/predict" \
     -F "file=@path/to/your/image.jpg"
```
Response example:
```json
{ "label": "Dog", "confidence": 92.34 }
```

---

## Troubleshooting

- **Model loading errors** – Ensure `image_CNN.keras` is present in the project root.
- **Port conflicts** – Change the port in the `uvicorn` command (e.g., `--port 8000`).
- **Missing dependencies** – Re‑install with `pip install .` or manually add any missing packages.

---

## License

This project is provided for educational purposes and is free to use under the MIT License.
