#import streamlit as st
#st.write("Привет, streamlit!")

import streamlit as st
import time
def long_operation():
    time.sleep(0.03)
my_bar = st.progress(0, text="Загрузка...")
for percent_complete in range(100):
    long_operation()
    my_bar.progress(percent_complete + 1, text="Загрузка...")
time.sleep(1)
my_bar.empty()
st.success("Загрузка завершена")


st.write("Вы уверены, что хотите остаться на странице?")
st.button("Да", type="primary")
st.button("Нет", type="secondary")

selection = st.selectbox("Выберите свой размер", ["XS", "S", "M", "L", "XL", "XXL"])
st.write("Размер:", selection)


selection = st.selectbox(
    "Какой у вас размер одежды?",
    ["XS", "S", "M", "L", "XL", "XXL"],
    index=None,
    placeholder="Выберите размер...",
)
st.write("Размер:", selection)