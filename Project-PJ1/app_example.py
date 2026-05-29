cache_data# app.py

#Быстрый запуск
# cd M:\YandexDisk\-Sync-\Dev\python_projects\skillfactory_python\final_project\ ; streamlit run .\app.py
# cd M:\YandexDisk\-Sync-\Dev\python_projects\skillfactory_python\final_project\ ; streamlit run .\app_example.py  

import streamlit as st
import sqlite3
import polars as pl
import plotly.express as px
from datetime import date # Импортируем date из datetime

DB_PATH = "data/weather.db"

st.set_page_config(page_title="WeatherInsight", layout="wide")
st.title("🌦️ WeatherInsight: Погодные тренды")

# Загрузка данных
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pl.read_database("SELECT * FROM weather ORDER BY date", conn)
    conn.close()
    return df

try:
    df = load_data()
except Exception as e:
    st.error("❌ Не удалось загрузить данные. Убедитесь, что база данных существует и доступна.")
    st.stop()

# Статистика по всем данным
st.subheader("📊 Общая статистика")
total_records = len(df)
unique_cities = df["city"].n_unique()
st.write(f"Всего записей: {total_records}")
st.write(f"Уникальных городов: {unique_cities}")

# Выбор города
cities = sorted(df["city"].unique().to_list())
selected_city = st.selectbox("Выберите город", cities)

city_data = df.filter(pl.col("city") == selected_city)
# df.write_csv('df_pl.csv')

# Разделение данных на исторические и прогноз
# Используем date.today() из Python
today = date.today()
# Преобразуем date в строку формата 'YYYY-MM-DD' для сравнения с колонкой 'date' в Polars
historical_data = city_data.filter(pl.col("date") < str(today))
forecast_data = city_data.filter(pl.col("date") >= str(today))

# График температуры для исторических данных
if not historical_data.is_empty():
    fig_temp_hist = px.line(
        historical_data.to_pandas(),
        x="date",
        y="avg_temp",
        title=f"Средняя температура в {selected_city} (исторические данные)",
        labels={"avg_temp": "Температура (°C)", "date": "Дата"}
    )
    st.plotly_chart(fig_temp_hist, use_container_width=True)

    # Статистика для исторических данных
    rainy_days_hist = historical_data["is_rainy"].sum()
    avg_temp_hist = historical_data["avg_temp"].mean()
    col1, col2 = st.columns(2)
    col1.metric("Средняя температура (история)", f"{avg_temp_hist:.1f}°C")
    col2.metric("Дождливых дней (история)", int(rainy_days_hist))

# График температуры для прогноза
if not forecast_data.is_empty():
    fig_temp_forecast = px.line(
        forecast_data.to_pandas(),
        x="date",
        y="avg_temp",
        title=f"Средняя температура в {selected_city} (прогноз)",
        labels={"avg_temp": "Температура (°C)", "date": "Дата"}
    )
    st.plotly_chart(fig_temp_forecast, use_container_width=True)

    # Статистика для прогноза
    rainy_days_forecast = forecast_data["is_rainy"].sum()
    avg_temp_forecast = forecast_data["avg_temp"].mean()
    col1, col2 = st.columns(2)
    col1.metric("Средняя температура (прогноз)", f"{avg_temp_forecast:.1f}°C")
    col2.metric("Дождливых дней (прогноз)", int(rainy_days_forecast))

# Аномалии (в данном случае - дни, отмеченные как дождливые)
# Ты можешь изменить условие для определения аномалий в зависимости от логики detect_anomalies
anomalies = city_data.filter(pl.col("is_rainy") == 1)  # Пример: аномалия - дождливый день
if not anomalies.is_empty():
    st.subheader("⚠️ Аномалии")
    st.write(f"Найдено {len(anomalies)} аномалий (дождливых дней) в {selected_city}.")
    st.dataframe(anomalies.to_pandas())
else:
    st.info("✅ Аномалии не обнаружены (по критерию 'дождливый день').")

# Таблица последних данных
st.subheader("📋 Последние данные")
st.dataframe(city_data.tail(10).to_pandas())