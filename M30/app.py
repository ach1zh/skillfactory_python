#M30-L8
#Практическое задание (HW)

'''
Получить данные от пользователя: 
- считывание суммы кредита
- процентной ставки
- срока кредита
- типа платежа по кредиту (аннуитетный и дифференциальный)
- считывание даты первого платежа 

+ обработку случаев неправильного ввода
+ использование механизмов условного рендеринга (if/else, st.expander(), st.rerun() и st.stop())
и добавление в таблицу даты каждого из платежей;

Вычислить:
- вычисление ежемесячного платежа по кредиту (для аннуитетного типа);
- формирование графика платежей по кредиту в виде таблицы со следующими столбцами:
    - остаток долга,
    - ежемесячный платеж,
    - процентная часть,
    - долговая часть,
    - остаток долга на конец периода;

Советы:

1. Для считывания суммы кредита, процентной ставки и срока кредита можно использовать st.text_input() или st.number_input().
2. Для считывания типа платежей могут подойти st.radio(), st.select_slider(), st.selectbox().
3. Для создания таблицы с графиком платежей можно сначала рассчитать все значения в цикле и сохранить в массивы, 
затем создать из них словарь, а после из словаря создать таблицу с помощью функции pd.DataFrame.from_dict().
4. Полезные материалы: Формулы для расчета обоих типов кредита с примерами и Готовый кредитный калькулятор для вдохновения.
    https://www.raiffeisen.ru/wiki/kak-rasschitat-procenty-po-kreditu/
    https://www.banki.ru/services/calculators/credits/
'''

import streamlit as st
import pandas as pd
import datetime


st.title('Практическое задание M30-L8')
st.markdown("### Кредитный калькулятор")
st.write("", "")

#Получаем данные от пользователя

credit_amount = st.number_input(
    label="Сумма кредита, руб.",
    min_value=0,
    max_value=1000000000,
    step=50000,
    value=200000,
    #help="Введите сумму кредита в рублях"
)
#credit_amount используется, активно перезаписывается
credit_amount_value = credit_amount

interest_rate = st.number_input(
    label="Процентная ставка.",
    min_value=1.0,
    value=12.0,
    step=0.1,
    format="%.1f",
    #help="Введите процентную ставку"
)

credit_period = st.number_input(
    label="Срок кредита, месяцы.",
    min_value=3,
    value=24,
    step=1,    
    help="Введите срок кредита в месяцах"
)

with st.expander("ℹ️ Подробнее о типах платежей"):
    st.markdown("""
    **Аннуитетный платёж:**
    * Фиксированная сумма каждый месяц
    * В начале срока большая часть — проценты
    * Удобно планировать бюджет

    **Дифференцированный платёж:**
    * Сумма уменьшается со временем
    * Основной долг делится на весь срок
    * Переплата меньше, чем при аннуитетном
    """)

credit_payment_type = st.selectbox(
    "Выберете тип платежей:",
    ["Аннуитетный платеж", "Дифференцированный платеж"],
    index=0,    
    placeholder="Выберете тип...",
)

credit_payment_type_is_annuity = False
credit_payment_type_is_differentiated = False

if credit_payment_type == 'Аннуитетный платеж':
    credit_payment_type_is_annuity = True
elif credit_payment_type == 'Дифференцированный платеж':
    credit_payment_type_is_differentiated = True
else:
    raise RuntimeError("CREDIT TYPE ERROR")


today = datetime.date.today()
credit_first_payment_date = st.date_input(
    "Выберите дату первого платежа",
    format="DD.MM.YYYY",
    value=today,
    min_value=today,    
)

#--------------------------------------------------
#Для теста
#предоставленные пользователем данные
#credit_amount = 200000
#interest_rate = 12.0
#credit_period = 24
#credit_payment_type_is_differentiated = False
#credit_payment_type_is_annuity = False
#credit_first_payment_date = "14.06.2026"
#--------------------------------------------------

#Переводим данные о дате платежа в формат pd.datetime
payment_date = pd.to_datetime(credit_first_payment_date, dayfirst=True)

#Вычисляем месячную процентную ставку в процентах
month_interest_rate = interest_rate / 12 / 100

#Данные для графика платежей
payment_schedule_data = []

#аннуитетный платеж
if credit_payment_type_is_annuity:

    #Вычисляем размер ежемесячного платежа по "классической" формуле и округляем
    monthly_payment = credit_amount * (month_interest_rate * (1 + month_interest_rate) ** credit_period) / ((1 + month_interest_rate) ** credit_period - 1)
    monthly_payment = round(monthly_payment, 2)
    
    # В цикле рассчитываем значения для каждого месяца
    for month in range(1, credit_period + 1):
        
        #Вычисляем долю процентов в ежемесячном взносе
        interest_percentage = round(credit_amount * month_interest_rate, 2)

        #Последний платёж считаем отдельно 
        if credit_amount < monthly_payment:
            # В последнем месяце платёж = остаток долга + проценты на остаток            
            monthly_payment = credit_amount + interest_percentage
            debt_portion = credit_amount
            debt_balance = 0.0
        else:
            #Вычисляем долговую часть
            debt_portion = round(monthly_payment - interest_percentage, 2)            
            #Вычисляем остаток долга на конец периода
            debt_balance = round(credit_amount - debt_portion,2)        
        
        #Собираем данные для таблицы
        payment_schedule_data.append({'month':month,'payment_date':payment_date.strftime("%d.%m.%Y"),'credit_amount':credit_amount,'monthly_payment':monthly_payment,'interest_percentage':interest_percentage,'debt_portion':debt_portion,'debt_balance':debt_balance})
        
        #Уменьшаем сумму основного долга на долговую часть
        credit_amount -= debt_portion
        #Смещаем дату
        payment_date = payment_date + pd.DateOffset(months=1)

#дифференцированный платеж
if credit_payment_type_is_differentiated:
    
    #Вычисляем долговую часть ежемесячного платежа
    debt_portion = round(credit_amount / credit_period, 2)

    # В цикле рассчитываем значения для каждого месяца
    for month in range(1, credit_period + 1):

        # В последнем месяце долговая часть = остаток долга
        if month == credit_period:            
            debt_portion = credit_amount
                
        #Вычисляем процентную часть ежемесячного платежа
        interest_percentage = round(credit_amount * month_interest_rate,2)        
        #Вычисляем ежемесячный платеж
        monthly_payment = round(debt_portion + interest_percentage,2)
        #Вычисляем остаток долга на конец периода
        debt_balance = round(credit_amount - debt_portion,2)
                
        #Собираем данные для таблицы
        payment_schedule_data.append({'month':month,'payment_date':payment_date.strftime("%d.%m.%Y"),'credit_amount':credit_amount,'monthly_payment':monthly_payment,'interest_percentage':interest_percentage,'debt_portion':debt_portion,'debt_balance':debt_balance})
                
        #Уменьшаем сумму основного долга
        credit_amount -= debt_portion
        #Смещаем дату
        payment_date = payment_date + pd.DateOffset(months=1)

payment_schedule = pd.DataFrame(payment_schedule_data)
payment_schedule.columns = ['Месяц','Дата платежа','Остаток долга','Ежемесячный платеж','Процентная часть','Долговая часть','Остаток долга на конец периода']

st.success("Расчет выполнен:")

#Отображаем результаты расчета
if credit_payment_type_is_annuity:
    st.markdown(f"""
    * Сумма кредита: {credit_amount_value:.2f} руб.
    * Ежемесячный платёж: {monthly_payment:.2f} руб.
    * Переплата: {payment_schedule['Процентная часть'].sum():.2f} руб.
    * Общая сумма выплат: {credit_amount_value + payment_schedule['Процентная часть'].sum():.2f} руб.
    """)
elif credit_payment_type_is_differentiated:
    st.markdown(f"""
    * Сумма кредита: {credit_amount_value:.2f} руб.
    * Ежемесячный платёж: от {payment_schedule['Ежемесячный платеж'].min():.2f} руб. до {payment_schedule['Ежемесячный платеж'].max():.2f} руб.
    * Переплата: {payment_schedule['Процентная часть'].sum():.2f} руб.
    * Общая сумма выплат: {credit_amount_value + payment_schedule['Процентная часть'].sum():.2f} руб.
    """)      

with st.expander("📋 Раскрыть график платежей"):
    st.dataframe(payment_schedule,width="stretch", hide_index=True)