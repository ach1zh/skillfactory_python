import streamlit as st
import pandas as pd
import datetime
import numpy as np
import time
import torch
from diffusers import StableDiffusionPipeline

my_str = "Привет, мир"
st.write(my_str)
st.download_button("Скачать",data="Привет, мир".encode("utf-8"),file_name="hi.txt",mime="text/plain")

@st.cache_data()
def get_data():
    df = pd.DataFrame(
        np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    time.sleep(3.0)
    return df

@st.cache_data()
def convert_for_download(df):
    time.sleep(3.0)
    return df.to_csv().encode("utf-8")

df = get_data()
csv = convert_for_download(df)

st.download_button(
    label="Загрузить таблицу CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv")

@st.cache_resource
def load_model():
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16,
            safety_checker=None, 
            requires_safety_checker=False)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        return pipe.to(device)
    except Exception as e:
        st.error(f"Ошибка загрузки модели: {e}")
        return None

st.title("Генератор картинок")
st.write("Введите описание на английском для лучших результатов")
prompt = st.text_area("Описание картинки:", "cute cat in sunglasses playing piano")
generate_btn = st.button("Создать картинку")

if generate_btn and prompt:
    with st.spinner("Генерирую... Это займет 10-30 секунд"):
        pipe = load_model()
        if pipe:
            image = pipe(prompt, num_inference_steps=20, guidance_scale=7.5).images[0]
            st.image(image, caption=prompt)
            # Сохранение
            image.save("generated_image.png")
            with open("generated_image.png", "rb") as file:
                st.download_button(
                    "Скачать картинку",
                    file,
                    file_name="generated_image.png",
                    mime="image/png")