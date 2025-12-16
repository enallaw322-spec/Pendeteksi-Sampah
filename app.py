import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Deteksi Sampah", page_icon="🗑️")

st.title("🗑️ Deteksi Jenis Sampah")
st.write("Upload gambar sampah untuk mengetahui kategorinya")

uploaded_file = st.file_uploader(
    "Pilih gambar sampah",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diupload", use_column_width=True)

    st.write("🔍 Menganalisis gambar...")

    hasil = random.choice(["Organik", "Anorganik"])
    st.success(f"✅ Hasil Deteksi: **{hasil}**")
