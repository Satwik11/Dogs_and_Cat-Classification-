
import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image,ImageOps
import cv2

st.set_option('deprecation.showfileUploaderEncoding',False)

st.title("Dog & Cat Classification")

@st.cache(allow_output_mutation = True)

def load_model():
  model = tf.keras.models.load_model("/content/drive/My Drive/MODEL .h5")
  return model

with st.spinner("Loading Model into memory..."):
  model = load_model()

file = st.file_uploader("Please upload image for classification",type=["jpg","png"])

def import_and_predict(image_data,model):
  size = (64,64)
  image = ImageOps.fit(image_data,size,Image.ANTIALIAS)
  img = np.asarray(image)
  img_reshape = img[np.newaxis,...]
  prediction = model.predict(img_reshape)

  return prediction

if file is None:
  st.text("Please upload image for classification")
else:
  image = Image.open(file)
  st.image(image,caption = "Classifying Animal Image",use_column_width = True)
  predictions = import_and_predict(image,model)
  class_names = ["Cat","Dog"]
  string = "This image is most likely is:"+class_names[np.argmax(predictions)]
  st.success(string)