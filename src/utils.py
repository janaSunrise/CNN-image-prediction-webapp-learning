import numpy as np
import streamlit as st

from tensorflow.keras.models import model_from_json
from tensorflow.keras.initializers import glorot_uniform

from keras import backend as keras_backend
from keras.applications.mobilenet import preprocess_input
from keras.applications import imagenet_utils
from keras.preprocessing import image
from keras.utils import CustomObjectScope

keras_backend.reset_uids()

model = 'src/model/model_json.json'
weights = 'src/model/mobilenetImagenet.h5'

with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    with open(model, 'r') as f:
        model = model_from_json(f.read())
        model.load_weights(weights)


@st.cache
def predict(img):
    img = image.load_img(img, target_size=(224, 224))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    result = model.predict(x)
    result_decode = imagenet_utils.decode_predictions(result)

    predictions = ""

    for (i, (predId, pred, prob)) in enumerate(result_decode[0]):
        predictions += f"{pred.replace('_', ' ')}: {prob * 100:.2f}%\n"

    return predictions
