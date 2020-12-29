"""
Core contributors: John Quitto-Graham, Hermes Bonilla, Kevin Hernandez, David.

Maintained by: Sunrit Jana.
"""

import time
from tempfile import NamedTemporaryFile

import streamlit as st
from PIL import Image

from utils import predict

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Image prediction using Tensorflow CNN")
st.header("Prediction for images using Tensorflow ImageNet")

uploaded_file = st.sidebar.file_uploader("Choose an image for prediction", type=["jpg", "png", "bmp", "jpeg"])
img_file = NamedTemporaryFile(delete=False)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_file.write(uploaded_file.getvalue())
    st.image(image, caption="Uploaded Image successfully.", use_column_width=True)

st.header("\n")

if st.sidebar.button("Click here to classify!"):
    if uploaded_file is None:
        st.sidebar.subheader("Please upload an image!")
    else:
        with st.spinner("Classifying..."):
            predictions = predict(img_file.name)
            time.sleep(2)

            st.success("Done!")
            st.header(predictions)
