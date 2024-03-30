import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/umm-maybe/AI-image-detector"
headers = {"Authorization": "Bearer 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"}

def query(file_content):
    response = requests.post(API_URL, headers=headers, data=file_content)
    return response.json()

def main():
    st.title("AI Image Detector")
    st.write("Upload an image to detect if it contains AI-generated content.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        st.write("")
        with st.spinner('Classifying...'):
            file_content = uploaded_file.read()
            output = query(file_content)
        
        
        if output[0]['label'] == 'artificial':
            st.markdown(
                f'<div style="padding: 20px; border-radius: 10px; background-color: #d1f7d1; border: 2px solid #4CAF50; text-align: center;">'
                f'<h2 style="color:green;">Artificial Image</h2>'
                f'<p style="color:green;">Probability Score: {output[0]["score"]}</p>'
                f'</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div style="padding: 20px; border-radius: 10px; background-color: #f7d1d1; border: 2px solid #FF5733; text-align: center;">'
                f'<h2 style="color:red;">Human Image</h2>'
                f'<p style="color:red;">Human Score: {output[1]["score"]}</p>'
                f'</div>',
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main()
