import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("model_sampah.h5")

# Label
labels = ["Organik", "Anorganik"]

st.title("🔍 Deteksi Jenis Sampah")
st.write("Upload gambar sampah untuk mengetahui kategorinya")

uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Gambar Terupload", width=250)

    img = img.resize((150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    prediction = model.predict(img_array)
    result = labels[int(prediction[0] > 0.5)]

    st.success(f"🎯 Jenis Sampah: **{result}**")
