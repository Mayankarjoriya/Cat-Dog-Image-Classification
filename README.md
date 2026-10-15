# Cat vs Dog CNN Classifier 🐱🐶

A machine learning image classification service that identifies whether an uploaded image is a **Cat** or a **Dog**, complete with confidence scores. Built with a convolutional neural network (CNN) in **TensorFlow/Keras**, served via a **FastAPI** backend, and presented through an interactive **Streamlit** web UI.

---

## 📁 Project Structure

```text
CNN_classifier/
├── images/             # Sample images for testing (cat.png, dog.png, etc.)
│   ├── cat.png
│   ├── dog.png
│   ├── image.png
│   └── Pasted image.png
├── frontend.py         # Streamlit web interface
├── main.py             # FastAPI backend API exposing /predict
├── test.py             # Standalone Python script for quick CLI model testing
├── image_CNN.keras     # Trained TensorFlow/Keras CNN model
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Lockfile for reproducible dependencies
├── .gitignore          # Git ignore specifications
└── README.md           # Project documentation
```

---

## ⚙️ Prerequisites

- **Python 3.12** (recommended; TensorFlow 2.x and Keras 3 may have stability issues on Python 3.13)
- [uv](https://docs.astral.sh/uv/) (recommended package manager) or standard `pip`

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mayankarjoriya/Cat-Dog-Image-Classification.git
cd Cat-Dog-Image-Classification
```

### 2. Install Dependencies

#### Using `uv` (Recommended)
```bash
uv sync
```

#### Using standard `venv` and `pip`
```bash
python3.12 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -e .
```

---

## 🏃 Running the Application

### Step 1: Start the FastAPI Backend

Run the backend server on port **8080**:

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
*(Or if your `.venv` is activated: `uvicorn main:app --host 0.0.0.0 --port 8080 --reload`)*

- API URL: `http://localhost:8080`
- Interactive API Docs (Swagger): `http://localhost:8080/docs`

### Step 2: Start the Streamlit Frontend

In a **separate terminal**, run the Streamlit app:

```bash
uv run streamlit run frontend.py
```
*(Or if your `.venv` is activated: `streamlit run frontend.py`)*

- Open `http://localhost:8501` in your browser.

---

## 🧪 Testing

### 1. Using the Streamlit UI
1. Open `http://localhost:8501`.
2. Upload any image (or select one from the `images/` directory).
3. Click **Predict** to view classification and confidence level.

### 2. Using cURL (API)
```bash
curl -X POST "http://localhost:8080/predict" \
     -F "file=@images/dog.png"
```
**Example Response:**
```json
{
  "label": "Dog",
  "confidence": 96.09
}
```

### 3. Using the Test Script
```bash
uv run python test.py
```

---

## 🛠️ Troubleshooting

- **Connection Refused (`[Errno 111]`)**:
  Ensure the FastAPI server is running specifically on port **8080** (`--port 8080`), matching the endpoint URL configured in `frontend.py`.
- **Remote End Closed Connection / Silent Crash**:
  Ensure you are running under **Python 3.12** in `.venv` rather than a system/Anaconda Python 3.13 environment (`uv run` ensures the correct environment is used).
- **Missing Model File**:
  Verify that `image_CNN.keras` is located in the project root directory.

---

## 📄 License

This project is licensed under the MIT License.
