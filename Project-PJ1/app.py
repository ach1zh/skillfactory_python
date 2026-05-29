#Практическое задание (PJ-1)

import streamlit as st
import sqlite3
import polars as pl
import pandas as pd
import plotly.express as px
import datetime

#Настройка streamlit
st.set_page_config(page_title="WeatherInsight", layout="wide")
st.title("🌦️ WeatherInsight: Погодные тренды")

DB_PATH = "data/weather.db"
#DB_PATH = "Project-PJ1\data\weather.db"

# Функция загрузки данных + кэширование
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pl.read_database("SELECT * FROM weather ORDER BY date", conn)
    conn.close()
    return df
#Загрузка данных из БД sqlite3
try:
    df = load_data()
except Exception as e:
    st.error(f"❌ Не удалось загрузить данные. Убедитесь, что база данных существует и доступна. Error: {str(e)}")
    st.stop()

#--------------------------------------------------
# Обработка столбца с датами. Переводим в to_datetime, убираем время 00:00:00
#--------------------------------------------------
df = df.with_columns(pl.col('date').str.to_datetime().dt.date())

#--------------------------------------------------
# Обработка пропусков
# Пропусков в данных нет. Но все равно напишем минимальную обработку.
# Удаляем строки, в которых пропущены данные в столбцах city или data. Остальные значения заполняем соседними данными.
#--------------------------------------------------
@st.cache_data
def handle_null_values(df: pl.DataFrame,columns:list[str],)-> pl.DataFrame:
    result_df = df.drop_nulls(subset=columns)
    #стратегия forward — замена пропущенных значений последним ненулевым значением.
    result_df = df.fill_null(strategy="forward")
    #так же можно использовать интерполяцию
    #result_df = df.interpolate()
    return result_df

df = handle_null_values(df,['city', 'date'])

#--------------------------------------------------
# Добавление новых категориальных признаков
#--------------------------------------------------
@st.cache_data
def add_categorical_attributes(df: pl.DataFrame)->pl.DataFrame:
    
    # Категория температуры ("холодно", "умеренно", "жарко").
    df = df.with_columns(
        pl.when(pl.col('avg_temp') <= 10)
        .then(pl.lit("холодно"))
        .when((pl.col('avg_temp') > 10) & (pl.col('avg_temp') <= 23))
        .then(pl.lit("умеренно"))
        .when(pl.col('avg_temp') > 23)
        .then(pl.lit("жарко"))
        .otherwise(pl.lit("не_определено"))
        .alias("temp_category")
    )

    # Уровень осадков ("без осадков", "небольшие", "сильные")
    # Статистика, что бы определить границы
    #print(df['total_precip'].describe())
    #print(df['total_precip'].value_counts().sort('count', descending=True))    
    df = df.with_columns(
        pl.when(pl.col('total_precip') == 0.0)
        .then(pl.lit("без осадков"))
        .when((pl.col('total_precip') >= 0.1) & (pl.col('total_precip') <= 1.9))
        .then(pl.lit("небольшие"))
        .when(pl.col('total_precip') > 1.9) #75%
        .then(pl.lit("сильные"))
        .otherwise(pl.lit("не_определено"))
        .alias("precip_category")
        )

    # Комфортность погоды (на основе дождя, температуры и ветра).
    # Статистика, что бы определить границы
    #print(df['avg_wind'].describe())
    #print(df['avg_wind'].value_counts().sort('count', descending=True)) 
    df = df.with_columns(
        # 1. Некомфортные условия
        pl.when(
            (pl.col('total_precip') > 1.9) |
            (pl.col('avg_temp') < 10) |
            (pl.col('avg_temp') > 30) |
            (pl.col('avg_wind') > 8))
        .then(pl.lit("некомфортно"))
        # 2. Комфортные условия
        .when(
            (pl.col('avg_temp').is_between(18, 28)) &
            (pl.col('avg_wind') <= 5)
        )
        .then(pl.lit("комфортно"))
        # 3. Умеренные условия
        .when(
        # Расширенный диапазон температур с умеренным ветром
        ((pl.col('avg_temp').is_between(14, 17) |
          pl.col('avg_temp').is_between(26, 32)) &
         (pl.col('avg_wind').is_between(0, 6))) |
        # Более прохладная/тёплая погода со слабым ветром
        ((pl.col('avg_temp').is_between(8, 13) |
          pl.col('avg_temp').is_between(29, 32)) &
         (pl.col('avg_wind') <= 3)) |
        # Идеальная температура с более сильным ветром
        ((pl.col('avg_temp').is_between(18, 25)) &
         pl.col('avg_wind').is_between(5, 8))
        )
        .then(pl.lit("умеренно"))
        # 4. Всё остальное — умеренно (на всякий случай)
        .otherwise(pl.lit("умеренно"))
        .alias("comfort_category")
    )

    #Статистика
    #print(df['comfort_category'].value_counts().sort('count', descending=True))
    return df

#Заупус функции для добавления новых категорий
df = add_categorical_attributes(df)

#--------------------------------------------------
# Фильтрация данных
#--------------------------------------------------
with st.sidebar:
    # Создаём контейнер для группировки элементов
    with st.container(border=False,horizontal=True,width="stretch",horizontal_alignment="center"):
        st.header("Фильтрация данных",text_alignment="center",divider=True)

    multiselect_city = st.multiselect(
        f"Фильтр по городу",
        options=list(sorted(df['city'].unique())),        
        placeholder="фильтр не задан",
        key = "multiselect_city"
    )    
    
    min_date = df['date'].min()
    max_date = df['date'].max()

    date_input_date = st.date_input(
        label = f"Фильтр по датам",        
        min_value=min_date,
        max_value=max_date,        
        value=(min_date,max_date),
        key="date_input_date" 
    )

    # Параметры для температуры
    min_temp = round(float(df['avg_temp'].min()), 1)
    max_temp = round(float(df['avg_temp'].max()), 1)

    slider_avg_temp = st.slider(
        label="Фильтр по температуре (°C)",
        min_value=min_temp,
        max_value=max_temp,
        value=(min_temp, max_temp),
        step=0.5,
        format="%.1f°C"
    )

    # Параметры для осадков
    min_precip = round(float(df['total_precip'].min()), 2)
    max_precip = round(float(df['total_precip'].max()), 2)

    slider_total_precip = st.slider(
        label="Фильтр по осадкам (мм)",
        min_value=min_precip,
        max_value=max_precip,
        value=(min_precip, max_precip),
        step=0.1,
        format="%.1f мм"
    )

    # Параметры для ветра
    min_wind = round(float(df['avg_wind'].min()), 1)
    max_wind = round(float(df['avg_wind'].max()), 1)

    slider_avg_wind = st.slider(
        label="Фильтр по скорости ветра (м/с)",
        min_value=min_wind,
        max_value=max_wind,
        value=(min_wind, max_wind),
        step=0.5,
        format="%.1f м/с"
    )

    selectbox_is_rainy = st.selectbox(
        "Фильтр признака дождя",
        options=['Да','Нет'],
        index=None,
        placeholder="фильтр не задан",
        key = "selectbox_is_rainy"
    )

    multiselect_temp_category = st.multiselect(
        f"Фильтр категории температуры",
        options=list(sorted(df['temp_category'].unique())),        
        placeholder="фильтр не задан",
        key = "multiselect_temp_category"
    )  

    multiselect_precip_category = st.multiselect(
        f"Фильтр категории осадков",
        options=list(sorted(df['precip_category'].unique())),        
        placeholder="фильтр не задан",
        key = "multiselect_precip_category"
    )  

    multiselect_comfort_category = st.multiselect(
        f"Фильтр категории комфортности погоды",
        options=list(sorted(df['comfort_category'].unique())),        
        placeholder="фильтр не задан",
        key = "multiselect_comfort_category"
    )


# -----------------------------------------------------
# Применение фильтров к данным
# -----------------------------------------------------

# Датафрейм не копируем, но на всякий случай сделаем так:
#filtered_df = df.clone()
filtered_df = df

# Распаковываем диапазон дат
if isinstance(date_input_date, tuple) and len(date_input_date) == 2:
    start_date, end_date = date_input_date
else:
    start_date, end_date = min_date, max_date

# Распаковываем диапазоны числовых параметров
min_temp_filter, max_temp_filter = slider_avg_temp
min_precip_filter, max_precip_filter = slider_total_precip
min_wind_filter, max_wind_filter = slider_avg_wind

# Применяем фильтры последовательно

# 1. По городу
if multiselect_city:
    filtered_df = filtered_df.filter(pl.col('city').is_in(multiselect_city))

# 2. По дате
filtered_df = filtered_df.filter(
    (pl.col('date') >= start_date) &
    (pl.col('date') <= end_date)
)

# 3. По температуре
filtered_df = filtered_df.filter(
    (pl.col('avg_temp') >= min_temp_filter) &
    (pl.col('avg_temp') <= max_temp_filter)
)

# 4. По осадкам
filtered_df = filtered_df.filter(
    (pl.col('total_precip') >= min_precip_filter) &
    (pl.col('total_precip') <= max_precip_filter)
)

# 5. По ветру
filtered_df = filtered_df.filter(
    (pl.col('avg_wind') >= min_wind_filter) &
    (pl.col('avg_wind') <= max_wind_filter)
)

# 6. По признаку дождя
if selectbox_is_rainy:
    if selectbox_is_rainy == 'Да':
        filtered_df = filtered_df.filter(pl.col('is_rainy') == 1)
    else:
        filtered_df = filtered_df.filter(pl.col('is_rainy') == 0)

# 7. По категории температуры
if multiselect_temp_category:
    filtered_df = filtered_df.filter(pl.col('temp_category').is_in(multiselect_temp_category))

# 8. По категории осадков
if multiselect_precip_category:
    filtered_df = filtered_df.filter(pl.col('precip_category').is_in(multiselect_precip_category))

# 9. По категории комфортности
if multiselect_comfort_category:
    filtered_df = filtered_df.filter(pl.col('comfort_category').is_in(multiselect_comfort_category))


# -----------------------------------------------------
# Создание вкладок
# -----------------------------------------------------
tab_show_data, tab_charts, tab_predict = st.tabs(["**Работа с таблицей**","**Работа с графиками**","**Прогноз**"])

#--------------------------------------------------
# Вывод табличных данных постранично, с фильтрацией
#--------------------------------------------------

with tab_show_data:

    # Инициализация в session_state переменной отображаемой страницы
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 1

    with st.container(border=False,horizontal=True,width=220,horizontal_alignment="center",vertical_alignment="bottom"):
        selected_page_size = st.selectbox(
        "Строк на странице",
        options=[10, 15, 20, 25, 50, 100],
        placeholder="Строк на странице ...",
        index=0  # по умолчанию 10 строк
        )

    #Общее количество страниц
    total_pages = filtered_df.height // selected_page_size + (1 if filtered_df.height % selected_page_size else 0)

    with st.container(border=False,horizontal=True,width=220,horizontal_alignment="distribute",vertical_alignment="bottom"):
        
        if st.button('⬅️ Назад') and st.session_state.current_page > 1:
                    st.session_state.current_page -= 1
        
        if st.button('Вперёд ➡️') and st.session_state.current_page < total_pages:
                    st.session_state.current_page += 1

    # Индикатор прогресса
    def calculate_progress(current_page, total_pages):
        if total_pages <= 0:
            return 0.0
        if current_page < 1:
            return 0.0
        if current_page > total_pages:
            return 1.0
        return current_page / total_pages

    progress = calculate_progress(st.session_state.current_page, total_pages)
    st.progress(progress)

    # Рассчитываем индексы для страниц
    start_idx = (st.session_state.current_page - 1) * selected_page_size
    end_idx = start_idx + selected_page_size

    #Отображение номера текущей страницы
    st.write(f'Страница {st.session_state.current_page} из {total_pages}')
    
    #Выводим данные постранично
    st.dataframe(filtered_df.slice(start_idx, end_idx - start_idx), use_container_width=True)

#--------------------------------------------------
# Визуализация данных
#--------------------------------------------------

with tab_charts:
    st.subheader("Графики распределения признаков", text_alignment="center", divider=True)

    # Маппинг пользовательских меток на имена колонок
    data_mapping = {
        "Температура": "avg_temp",
        "Количество осадков": "total_precip",
        "Скорость ветра": "avg_wind"
    }

    # Единицы измерения для подписей осей
    units_mapping = {
        "Температура": "°C",
        "Количество осадков": "мм",
        "Скорость ветра": "м/с"
    }

    with st.container(border=False, horizontal=True, horizontal_alignment="center", vertical_alignment="bottom"):
        selectbox_graph_data = st.selectbox(
            label="Данные для графика",
            options=["Температура", "Количество осадков", "Скорость ветра"],
            index=None,
            placeholder="Выберите данные для графика ...",
            key="selectbox_graph_data"
        )

        selectbox_graph_type = st.selectbox(
            label="Тип графика",
            options=["Гистограмма", "Коробчатая диаграмма"],
            index=None,
            placeholder="Выберите тип графика ...",
            key="selectbox_graph_type"
        )

    # Функции построения графиков распределения
    # Гистограмма
    def generate_graph_histogram(data_frame, x_data, title, unit):
        fig_histogram = px.histogram(
            data_frame=data_frame,
            x=x_data
        )
        fig_histogram.update_layout(
            title={
                'text': f'Распределение параметра: {title.lower()}',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title=f'{title} ({unit})',
            yaxis_title='Частота (количество наблюдений)',
            font=dict(size=12),
            margin=dict(l=60, r=30, t=50, b=60),
            showlegend=True,
            bargap=0.05
        )
        return fig_histogram
    
    #Коробчатая диаграмма
    def generate_graph_box(data_frame, x_data, title, unit):
        fig_box = px.box(
            data_frame=data_frame,
            x=x_data
        )
        fig_box.update_layout(
            title={
                'text': f'Коробчатая диаграмма параметра: {title.lower()}',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title=f'{title} ({unit})'
        )
        return fig_box

    # Отображение графика
    if selectbox_graph_data and selectbox_graph_type:
        
        # Получаем имя колонки и единицу измерения
        col_name = data_mapping[selectbox_graph_data]
        unit = units_mapping[selectbox_graph_data]

        # Выбираем функцию построения графика
        if selectbox_graph_type == 'Гистограмма':
            fig = generate_graph_histogram(filtered_df, col_name, selectbox_graph_data, unit)
        else:  # 'Коробчатая диаграмма'
            fig = generate_graph_box(filtered_df, col_name, selectbox_graph_data, unit)

        # Выводим график
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Выберите данные и тип графика для отображения.")

    st.subheader("Сравнение погодных показателей между городами",text_alignment="center",divider=True)

    with st.container(border=False, horizontal=True, horizontal_alignment="center", vertical_alignment="bottom"):
        
        multiselect_comparison_city = st.multiselect(
        f"Фильтр по городу",
        options=list(sorted(filtered_df['city'].unique())),        
        placeholder="фильтр не задан",
        key = "multiselect_comparison_city"
        )
        
        selectbox_comparison_graph_data = st.selectbox(
            label="Данные для графика",
            options=["Температура", "Количество осадков", "Скорость ветра"],
            index=None,
            placeholder="Выберите данные для графика ...",
            key="selectbox_comparison_graph_data"
        )

        selectbox_comparison_graph_type = st.selectbox(
            label="Тип графика",
            options=["Линейный график", "Столбчатая диаграмма"],
            index=None,
            placeholder="Выберите тип графика ...",
            key="selectbox_comparison_graph_type"
        )

    #Применяем фильтр городов
    if multiselect_comparison_city:
        filtered_comparison_city_df = filtered_df.filter(pl.col('city').is_in(multiselect_comparison_city))
    else:
        # если города не выбраны, используем все данные
        filtered_comparison_city_df = filtered_df
    
    # Функция для построения линейного графика (откладываем дату по X, цветом выделяем город)
    def generate_line_chart(data_frame, y_data, title, unit):
        fig = px.line(
            data_frame,
            x='date',
            y=y_data,
            color='city',
            #title=f'Динамика {title.lower()} по датам',
            labels={
                'date': 'Дата',
                y_data: f'{title} ({unit})',
                'city': 'Город'
            }
        )
        fig.update_layout(
            title={
                'text': f'Изменение  параметра "{title.lower()}" по датам',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title='Дата',
            yaxis_title=f'{title} ({unit})',
            font=dict(size=12),
            margin=dict(l=60, r=30, t=50, b=60),
            legend_title_text='Город'
        )
        return fig

    # Функция для построения столбчатой диаграммы (откладываем дату по X,цветом выделяем город)
    def generate_bar_chart(data_frame, y_data, title, unit):
        fig = px.bar(
            data_frame,
            x='date',
            y=y_data,            
            labels={                
                y_data: f'{title} ({unit})'
            },
            color='city'
        )
        fig.update_layout(
            title={
                'text': f'Значения параметра "{title.lower()}" по городам и датам',
                'x': 0.5,
                'xanchor': 'center'
            },
            xaxis_title='Дата',
            yaxis_title=f'{title} ({unit})',
            font=dict(size=12),
            margin=dict(l=60, r=30, t=50, b=60)
        )
        return fig

    # Отображение графика
    if selectbox_comparison_graph_data and selectbox_comparison_graph_type:
        # Получаем имя колонки и единицу измерения
        col_name = data_mapping[selectbox_comparison_graph_data]
        unit = units_mapping[selectbox_comparison_graph_data]
        
        # Выбираем функцию построения графика
        if selectbox_comparison_graph_type == 'Линейный график':
            fig = generate_line_chart(
                filtered_comparison_city_df,
                col_name,
                selectbox_comparison_graph_data,
                unit
            )
        else:  # 'Столбчатая диаграмма'
            fig = generate_bar_chart(
                filtered_comparison_city_df,
                col_name,
                selectbox_comparison_graph_data,
                unit
            )

        # Показываем график
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Выберите параметр, тип графика и города для отображения.")

#--------------------------------------------------
# Прогнозирование
#--------------------------------------------------

with tab_predict:
    #Заголовок
    st.subheader("Прогнозирование", text_alignment="center", divider=True)

    # Элементы пользовательского интерфейса
    with st.container(border=False, horizontal=True, horizontal_alignment="center", vertical_alignment="bottom"):

        selectbox_predict_data = st.selectbox(
            label="Данные для прогноза",
            options=["Температура", "Количество осадков", "Скорость ветра"],
            index=None,
            placeholder="Выберите данные для прогноза ...",
            key="selectbox_predict_data"
        )
        selectbox_predict_city = st.selectbox(
            label="Выберите город",
            index=None,
            options=sorted(filtered_df['city'].unique().to_list()),
            placeholder="Выберите данные для прогноза ...",
            key="selectbox_predict_city"
        )

        number_input_windows_size = st.number_input(
            label="Окно скользящего среднего", 
            value=7,
            min_value=2,
            max_value=31,
            step=1,
            placeholder="Введите значение ..."
        )

        number_input_forecast_days = st.number_input(
            label="Колличество прогнозируемых дней", 
            value=7,
            min_value=1,
            max_value=7,
            step=1, 
            placeholder="Введите значение ..."
        )

    # Проверяем, что все параметры выбраны
    if not selectbox_predict_data or not selectbox_predict_city:
        st.info("Выберите параметры для прогноза.")
    else:
        # Сопоставляем имена выбранных параметров
        target_col = data_mapping[selectbox_predict_data]
        unit = units_mapping[selectbox_predict_data]
        title = selectbox_predict_data.lower()

        # Фильтрация данных по выбранному городу
        city_df = filtered_df.filter(pl.col('city') == selectbox_predict_city)        

        # Подготовка данных для прогноза. Переводим в pandas, устанавливаем дату в качестве индекса
        city_pandas_df = city_df.to_pandas()
        city_pandas_df['date'] = pd.to_datetime(city_pandas_df['date'])
        city_pandas_df = city_pandas_df.sort_values('date')
        city_pandas_df = city_pandas_df.set_index('date')
        
        def get_forecast_data(df, target_column, window_size=7, forecast_days=7):
            
            """
            Simple Moving Average (SMA)
            Рассчитывает простой итеративный прогноз на основе скользящего среднего для выбранного столбца данных.
            Прогноз на каждый последующий день строится на основе средних значений за предыдущие дни.
            Дата в df обязательно должна быть индексом в формате DatetimeIndex (panads)
            """

            # Выделяем колонку как Series
            series_to_forecast = df[target_column].copy()
            
            # Цикл по количеству дней прогноза
            for _ in range(forecast_days):
                # Считаем скользящее среднее, берем самое последнее значение — это и есть наш прогноз на следующий день
                next_forecast_value = series_to_forecast.rolling(window=window_size, min_periods=1).mean().iloc[-1]

                # Значения "Количество осадков" и "сила ветра" не могут быть меньше нуля. Устанавливаем ограничения. 
                if target_column in ["total_precip", "avg_wind"]:
                    next_forecast_value = max(0, next_forecast_value)

                # Определяем дату для прогноза = плюс 1 день к последней дате в текущем df
                next_date = series_to_forecast.index[-1] + pd.Timedelta(days=1)
                
                #Добавляем новую дату и прогнозное значение в конец Series
                series_to_forecast.loc[next_date] = next_forecast_value

            # Возвращаем Series с индексом дат
            return series_to_forecast

        # Расчёт прогноза
        forecast_series = get_forecast_data(
            df=city_pandas_df,
            target_column=target_col,
            window_size=number_input_windows_size,
            forecast_days=number_input_forecast_days
        )

        # Сборка итогового DataFrame с прогнозом        
        last_real_date = city_pandas_df.index[-1]
        result_df = pd.DataFrame({
            #'Дата': forecast_series.index.strftime('%d-%m-%Y'),
            'Дата': forecast_series.index,
            'Значение': forecast_series.values,
            'Тип': ['Реальные данные' if date <= last_real_date else 'Прогноз' for date in forecast_series.index]
        })

        # Выводим таблицу с прогнозом
        st.dataframe(result_df.tail(number_input_forecast_days + 7), use_container_width=True)

        # Построение графика
        fig = px.line(
            result_df,
            x='Дата',
            y='Значение',
            color='Тип',
            color_discrete_map={
                'Реальные данные': 'blue',
                'Прогноз': 'orange'
            },
            line_dash='Тип',
            markers=False,
            title=f"{selectbox_predict_data} в {selectbox_predict_city}",
            labels={'Значение': f'{selectbox_predict_data} ({unit})', 'Дата': 'Дата'}
        )

        # Отображение графика
        st.plotly_chart(fig, use_container_width=True)