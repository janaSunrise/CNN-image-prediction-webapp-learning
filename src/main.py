"""
Core contributors: John Quitto-Graham, Hermes Bonilla, Kevin Hernandez, David.

Maintained by: Sunrit Jana.
"""

# -- Imports -- #
import time
from tempfile import NamedTemporaryFile

import streamlit as st
from PIL import Image

from utils import predict

# -- Config the warnings -- #
st.set_option('deprecation.showfileUploaderEncoding', False)

# -- The views -- #
st.title("Image prediction using Tensorflow CNN")
st.header("Prediction for images using Tensorflow ImageNet")

# -- File logic -- #
uploaded_file = st.sidebar.file_uploader("Choose an image for prediction", type=["jpg", "png", "bmp", "jpeg"])
img_file = NamedTemporaryFile(delete=False)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_file.write(uploaded_file.getvalue())
    st.image(image, caption="Uploaded Image successfully.", use_column_width=True)

st.header("\n")

# -- Classification logic -- #
if st.sidebar.button("Click here to classify!"):
    if uploaded_file is None:
        st.sidebar.subheader("Please upload an image!")
    else:
        with st.spinner("Classifying..."):
            predictions = predict(img_file.name)
            time.sleep(2)

            st.success("Done!")
            st.header(predictions)
