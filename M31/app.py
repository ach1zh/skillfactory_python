#M31-L8
#Практическое задание (HW)

# быстрый запуск
# cd M:\YandexDisk\-Sync-\Dev\python_projects\skillfactory_python\M31\ ; streamlit run .\app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Практическое задание M31-L8')
st.markdown("### Анализ CSV файлов")
st.write("", "")

#Настройка страницы
st.set_page_config(
        page_title="Анализ CSV файлов",
        page_icon="📊",
        #layout="wide",
        )

# Функция для сброса состояния и кешей
def reset_session_and_cache():    
    # Очищаем session_state
    for key in list(st.session_state.keys()):
        del st.session_state[key]    
    # Сбрасываем кеши
    st.cache_data.clear()
    st.cache_resource.clear()

#Функция безопасной загрузки таблицы из CSV
@st.cache_data() #кэшируем
def safe_load_table(file, verbose=False, delimiter=None):
    df = None
    try:
        if file.name.endswith(".csv"):
            encodings = ["utf-8","cp1251","latin_1","utf_16","koi8_r"] # топ пять популярных кодировок
            for enc in encodings:
                try:
                    if delimiter is not None:
                        df = pd.read_csv(file, encoding=enc, sep=delimiter)
                        break
                    else:
                        df = pd.read_csv(file, encoding=enc)
                        break
                except UnicodeDecodeError:
                    file.seek(0) # Сбрасываем позицию чтения        
    except pd.errors.EmptyDataError:
        if verbose:
            st.error("Ошибка: Файл пустой")
            st.stop()
    except Exception as e:
        if verbose:
            st.error(f"Неожиданная ошибка: {str(e)}")
    return df

#Разделитель. Автовыбор или ручной ввод.

# Создаём две колонки: для радиокнопок и для поля ввода
col1, col2 = st.columns([2, 3])  # Первая колонка шире для радиокнопок

with col1:
    # Радиокнопки для выбора способа определения разделителя
    delimiter_choice = st.radio(
        "Определение разделителя",
        ["Автоопределение", "Ввести разделитель вручную"],
    )

with col2:
    # Поле ввода появляется только если выбрана опция ручного ввода
    if delimiter_choice == "Ввести разделитель вручную":
        delimiter = st.text_input(
            "Введите разделитель:",            
        ).strip()

        # Проверка на пустой ввод
        if not delimiter:
            st.warning("Разделитель не может быть пустым")
            delimiter = None
        else:
            st.success(f"Выбран разделитель: '{delimiter}'")
    else:
        # Если автоопределение — показываем сообщение
        st.info("Будет использован автоматически определённый разделитель")
        delimiter = None

#Загрузка CSV-файла
file = st.file_uploader(
    "Загрузите CSV файл",
    accept_multiple_files=False,
    type=["csv"],
    #При загрузке файла так же сбрасываем кеши и удаляем все st.session_state
    on_change=reset_session_and_cache
    )

if file is None:
    st.warning("Пожалуйста, загрузите CSV-файл для начала работы.")
    st.stop()

#Получаем данные в виде датафрейма
df = None
df = safe_load_table(file, verbose=True,delimiter=delimiter)

#Сохраняем итоговый датафрейм в st.session_state
if "df" not in st.session_state:
    st.session_state["df"] = df

st.success("Файл успешно загружен")

# Преобразование столбцов с датами в формат pd.to_datetime()
with st.expander("Преобразование столбцов, содержащих дату и время"):
    column_to_dt_format = st.multiselect(
        "Если требуется, выберите столбцы, которые необходимо преобразовать",
        st.session_state.df.columns.tolist(),
        placeholder="Выберете столбцы ..." 
    )

    if column_to_dt_format:  # Если выбраны столбцы для преобразования
        
        # Опция 1: DayFirst (день перед месяцем — европейский формат)
        day_first_option = st.checkbox(
            "Установить опцию DayFirst",
            value=False,
            key="day_first_option"
        )

        # Опция 2: Пользовательский формат — чекбокс для активации поля ввода
        use_custom_format = st.checkbox(
            "Использовать пользовательский формат даты",
            value=False,
            key="use_custom_format_checkbox"
        )

         # Поле ввода появляется только если чекбокс активирован
        custom_format = ""
        if use_custom_format:
            custom_format = st.text_input(
                "Укажите формат даты (например, '%Y-%m-%d' или '%d.%m.%Y')",
                value="",
                placeholder="Введите формат даты...",
                key="custom_format_input"
            ).strip()
            # Подсказка с популярными форматами
            st.caption("Популярные форматы: %Y-%m-%d, %d.%m.%Y, %m/%d/%Y, %Y-%m-%d %H:%M:%S")
        
        # Кнопка для запуска преобразования
        if st.button("Преобразовать выбранные столбцы", key="convert_dates_btn"):            
            for col in column_to_dt_format:
                try:
                    # Проверка типа данных столбца
                    if st.session_state.df[col].dtype not in ['str','string','object']:
                        st.error(f"Столбец '{col}' имеет тип {st.session_state.df[col].dtype}. Преобразование в дату невозможно.")
                        continue

                    # Параметры для to_datetime
                    # errors='raise' гарантирует, что нераспознанные значения вызовут ошибку.
                    kwargs = {'errors': 'raise'} 
                    #kwargs = {'errors': 'coerce'} # Значения NAT вместо ошибки                    

                    # Добавляем параметры в зависимости от выбранных опций
                    if day_first_option:
                        kwargs['dayfirst'] = True

                    if custom_format:
                        kwargs['format'] = custom_format

                    # Выполняем преобразование
                    st.session_state.df[col] = pd.to_datetime(st.session_state.df[col], **kwargs)

                    st.success(f"Столбец '{col}' преобразован в формат datetime")

                except Exception as e:
                    st.error(f"Ошибка при преобразовании столбца '{col}': {str(e)}")
    else:
        st.info("Выберите столбцы для преобразования")


#Выводим загруженную таблицу
st.dataframe(st.session_state.df)

tab1, tab2 = st.tabs(["Статистический анализ", "Построение графиков"])

# Выводим форму
with tab1:

    # Создаём две колонки
    col3, col4 = st.columns([2, 3])  # Первая колонка шире

    with col3:
        st.markdown("##### Статистический анализ для числовых данных")
        numeric_columns_only = st.checkbox(
            "Скрыть нечисловые столбцы",
            value=False,
            key="checkbox_tab1"
        )

    with col4:
        # Определяем список столбцов в зависимости от состояния чекбокса numeric_columns_only
        if numeric_columns_only:
            # Фильтруем только числовые столбцы
            available_columns = st.session_state.df.select_dtypes(include=['number']).columns.tolist()
            if not available_columns:
                st.warning("В данных нет числовых столбцов!")
                selected_column = None
            else:
                selected_column = st.selectbox(
                    "Выберите столбец таблицы для анализа",
                    options=available_columns,
            index=None,
            placeholder="Выбрать столбец ...",
            key = "selectbox_1_tab1"
        )
        else:
            # Показываем все столбцы
            selected_column = st.selectbox(
                "Выберите столбец таблицы для анализа",
                options=st.session_state.df.columns.tolist(),
                index=None,
                placeholder="Выбрать столбец ...",
                key = "selectbox_2_tab1"
            )
        
    #Пользователь выбрал столбец
    if selected_column:    
        #Проверяем тип данных
        column_dtype = st.session_state.df[selected_column].dtype    
        #Если тип данных числовой, выводим статистику (describe())
        if pd.api.types.is_numeric_dtype(column_dtype):
            st.success(f"Тип данных числовой ({column_dtype}). Данные успешно обработаны")        
            describe = st.session_state.df[selected_column].describe()
            st.dataframe(describe)            
            
            fig = go.Figure()
            fig.add_trace(go.Histogram(
                x=st.session_state.df[selected_column],
                marker=dict(
                    color='lightblue',
                    line=dict(color='darkblue', width=1)
                ),
                name='Распределение'
            ))

            fig.update_layout(
                title={
                    'text': f'Гистограмма распределения: {selected_column}',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                xaxis_title=selected_column,
                yaxis_title='Частота (количество наблюдений)',
                font=dict(size=12),
                margin=dict(l=60, r=30, t=50, b=60),
                showlegend=True,
                bargap=0.05  # Промежуток между столбцами
            )

            st.plotly_chart(fig)
        #Если тип данных не числовой, то выводим ошибку
        else:
            st.error("Тип столбца не является числовым, выберете другой столбец")

with tab2:

    available_columns_tab2 = st.session_state.df.select_dtypes(include=['number','datetime','datetime64']).columns.tolist()    
    
    if not available_columns_tab2:
        st.warning("В данных нет числовых столбцов!")
        selected_column = None
    else:
        
        st.info("Выбор возможен только из числовых столбцов и столбцов с датами")

        # Создаём две колонки
        col5, col6 = st.columns(2)
        
        with col5:
            selected_column_tab2_1 = st.selectbox(
                "Выберите столбец таблицы для графика (ось X)",
                key="selectbox_1_tab2",
                options=available_columns_tab2,
                index=None,
                placeholder="Выбрать столбец ..."
            )

        with col6:
            selected_column_tab2_2 = st.selectbox(
                "Выберите столбец таблицы для графика (ось Y)",
                key="selectbox_2_tab2",
                options=available_columns_tab2,
                index=None,
                placeholder="Выбрать столбец ..."
            )
    
    chart_types = ["Диаграмма рассеяния","Линейный график","Столбчатая диаграмма"]
    
    selected_column_tab2_3 = st.selectbox(
        "Выберете тип графика",
        key="selectbox_3_tab2",
        options=chart_types,
        index=None,
        placeholder="Выбрать тип графика ..."
    )

    if selected_column_tab2_1 is None or selected_column_tab2_2 is None or selected_column_tab2_3 is None:
        st.warning("Данные для графика не выбраны")
    else:     
        #Линейный график
        if selected_column_tab2_3 == "Линейный график":
            x_data = st.session_state.df[selected_column_tab2_1]
            y_data = st.session_state.df[selected_column_tab2_2]
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines',))
            fig.update_layout(
                title=f'График зависимости {selected_column_tab2_2} от {selected_column_tab2_1}',
                xaxis_title=selected_column_tab2_1,  # Имя столбца по оси X
                yaxis_title=selected_column_tab2_2   # Имя столбца по оси Y
            )
            st.plotly_chart(fig)        
        
        #Диаграмма рассеяния
        elif selected_column_tab2_3 == "Диаграмма рассеяния":
            x_data = st.session_state.df[selected_column_tab2_1]
            y_data = st.session_state.df[selected_column_tab2_2]
            fig = go.Figure()
            fig.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            mode='markers',
            marker=dict(
                color='blue',
                size=8,
                opacity=0.7,  # Прозрачность точек для лучшей читаемости при наложении
                line=dict(width=1, color='darkblue')  # Контур вокруг точек
            ),
            name='Данные'
            ))

            fig.update_layout(
                title={
                    'text': f'Диаграмма рассеяния: {selected_column_tab2_2} от {selected_column_tab2_1}',
                    'x': 0.5,
                    'xanchor': 'center'
                },
                xaxis_title=selected_column_tab2_1,
                yaxis_title=selected_column_tab2_2,
                font=dict(size=12),
                margin=dict(l=60, r=30, t=50, b=60),
                hovermode='closest',  # Подсказки при наведении на ближайшую точку
                showlegend=True
            )
            st.plotly_chart(fig)

        #Столбчатая диаграмма
        elif selected_column_tab2_3 == "Столбчатая диаграмма":
            
            #Можно запрашивать данные у пользователья и по-разному агрегировать данные. Сделаем это в следующей версии приложения.
            #agg_data = st.session_state.df.groupby(selected_column_tab2_1, as_index=False)[selected_column_tab2_2].sum()
            #x_data = agg_data[selected_column_tab2_1]
            #y_data = agg_data[selected_column_tab2_2]
            
            x_data = st.session_state.df[selected_column_tab2_1]            
            y_data = st.session_state.df[selected_column_tab2_2]
            fig = go.Figure()
            #fig.add_trace(go.Bar(x=x_data, y=y_data,marker={'color' :'blue'}))
            fig.add_trace(go.Bar(x=x_data, y=y_data,))
            fig.update_layout(
                title=f'График зависимости {selected_column_tab2_2} от {selected_column_tab2_1}',
                xaxis_title=selected_column_tab2_1,  # Имя столбца по оси X
                yaxis_title=selected_column_tab2_2,   # Имя столбца по оси Y
                #xaxis=dict(tickangle=-45),
            )
            st.plotly_chart(fig)
        
        #Сохранить график как изображение - ресурсоёмкая операция. Выполняем только по нажатию на кнопку.
        
        # Флаг готовности изображения
        image_ready = 'current_plot_image' in st.session_state

        if not image_ready:
            if st.button("Конвертировать график в изображение для загрузки"):
                with st.spinner("Генерация изображения... Это может занять несколько секунд"):
                    # Генерация только по нажатию
                    st.session_state.current_plot_image = fig.to_image(
                        format="png",
                        width=800,
                        height=600,
                        scale=2
                    )
                    st.rerun()  # Обновляем интерфейс, чтобы показать кнопку скачивания
        else:
            # Показываем кнопку скачивания, если изображение сгенерировано
            st.download_button(
                label="📥 Скачать график как изображение",
                data=st.session_state.current_plot_image,
                file_name=f"график_{selected_column_tab2_3.lower().replace(' ', '_')}.png",
                mime="image/png",
                on_click=lambda: st.session_state.pop('current_plot_image', None)  # Очистка после скачивания
            )