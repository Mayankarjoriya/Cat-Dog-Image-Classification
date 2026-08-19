import streamlit as st
import requests

st.set_page_config(page_title="Cat vs Dog Classifier", page_icon="🐾")
st.title("🐱 Cat vs Dog Classifier")
st.sidebar.title("About")

left_col, right_col = st.columns(2)

with left_col:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    st.toast("Please upload an image of a cat or dog to get a prediction.", icon="ℹ️")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", width="stretch")

        if st.button("Predict", width="stretch"):
            st.spinner("Predicting... Please wait.")
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

            try:
                response = requests.post("http://localhost:8080/predict", files=files, timeout=30)
                try:
                    result = response.json()
                except ValueError:
                    result = None

                if response.status_code == 200 and isinstance(result, dict):
                    st.session_state.prediction_result = result
                else:
                    st.session_state.prediction_result = {
                        "error": f"API Error: {response.text or 'Invalid response from server'}"
                    }
            except requests.RequestException as exc:
                st.session_state.prediction_result = {"error": f"Request failed: {exc}"}

with right_col:
    st.subheader("Your Result")
    if "prediction_result" in st.session_state:
        result = st.session_state.prediction_result

        if "error" in result:
            st.error(result["error"])
        else:
            
            st.success(f"It's a {result.get('label', 'unknown class')}")
            # st.write(f"Confidence: {result.get('confidence', 0):.4f}%")
            st.metric(label="Confidence", value=f"{result.get('confidence', 0):.2f}%")
            st.progress(result.get("confidence", 0) / 100)
    else:
        st.info("Upload an image on the left and click Predict to see the result here.")