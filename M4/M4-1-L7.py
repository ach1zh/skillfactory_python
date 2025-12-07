#M4-1-L7

#Задание 19.7.1 (External resource)

"""
Функция должна принимать на вход список вопросов от пользователей и возвращать список ответов отдела поддержки.

Приоритет означает следующее: если в сообщении содержатся все три ключевых слова,
то ответное сообщение должно соответствовать слову, которые имеет наивысший приоритет:

Ваша задача: только реализовать функцию customer_support_simulator, вызывать её не нужно.
"""
from itertools import count
from struct import pack_into

"""
Ключевое слово	    Ответ	                                                                                    Приоритет
Ошибка	            Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.	Самый высокий
Заказ	            Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.	                Высокий
Вернуть	            Вы можете вернуть товар в течение 14 дней с момента получения.	                            Низкий
Нет ключевых слов	Благодарим вас за обращение. Ваш вопрос передан специалистам.	                            Если не было ключевых слов
"""


def customer_support_simulator(questionsList):

    answers = []

    # 0 - нет приоритета, 1 - самый высокий приоритет
    dict_db = {"Ошибка":[1,"Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой."],"Заказ":[2,"Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен."],"Вернуть":[3,"Вы можете вернуть товар в течение 14 дней с момента получения."],"None":[0,"Благодарим вас за обращение. Ваш вопрос передан специалистам."]}

    for question in questionsList:

        temp_answerList = {}

        for key, value in dict_db.items():
            if key.lower() in question.lower():
                #print(str(key.lower() in question.lower()) + " --> " + key.lower() + "<->" + question.lower())
                temp_answerList[key] = dict_db[key]

        if not bool(temp_answerList):
            #print(dict_db['None'][1])
            answers.append(dict_db['None'][1])
        else:
            #print(max(temp_answerList, key=temp_answerList.values()[0]))
            #print(temp_answerList)
            #print(temp_answerList.items())

            """
            Доступ к значению приоритета
            for elem in dict_db.items():
            print(elem[1][0])
            """

            #for elem in temp_answerList.items():
            #    print(elem[1][0])
            #    #print(elem[1][1])

            #print("\n---")
            #print(min(temp_answerList.items(), key = lambda x: x[1][0]))
            #print("\n---")
            answer = min(temp_answerList.items(),key = lambda x: x[1][0])
            answers.append(answer[1][1])
    return answers

print("\n----->")
questions = ["Это какая-то ошибка. Почему мой заказ еще не пришел? Я хочу вернуть средства."]
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')

# Question №1: Это какая-то ошибка. Почему мой заказ еще не пришел? Я хочу вернуть средства.
# Answer: Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.

print("\n----->\n")
questions = ["Почему мой заказ еще не пришел?", "Возникла ошибка при оплате", "Как мне вернуть товар?"]
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')

print("\n----->\n")
questions = ["фывфывфывфвы"]
answers = customer_support_simulator(questions)
for i, answer in enumerate(answers):
   print(f'Question №{i + 1}: {questions[i]}')
   print(f'Answer: {answer}')

#  Question №1: Почему мой заказ еще не пришел?
# Answer: Ваш заказ обрабатывается. Мы уведомим вас, как только он будет отправлен.
# Question №2: Возникла ошибка при оплате
# Answer: Мы извиняемся за причиненные неудобства. Наши специалисты уже работают над этой ошибкой.
# Question №3: Как мне вернуть товар?
# Answer: Вы можете вернуть товар в течение 14 дней с момента получения.


#Задание 19.7.2 (External resource)
print("\n----------------------------------------\n>")

"""
Напишите функцию, которая принимает такой список списков, и ключевые аргументы, которые определяют, 
какую статистику нужно вернуть: общий доход или количество проданных единиц каждого товара.
"""
#["название товара", количество, цена за единицу]


#def sales_stats(dataList,revenue=False,quantity=False):
#Чтобы пройти автотест
def sales_stats(dataList, revenue=True, quantity=True):
    if not bool(revenue) and not bool(quantity):
        print("None_None_None_None_None")
        return None
    else:

        if bool(revenue):
            result_revenue = 0
            for data in dataList:
                result_revenue += (data[1]*data[2])
            # or
            # result = (sum((map(lambda x: x[1]*x[2], sales_data))), None)
        else:
            result_revenue = None

        if bool(quantity):
            result_quantity = {}
            for i in dataList:
                count = 0
                for j in dataList:
                    if i[0] == j[0]:
                        count += j[1]
                result_quantity[i[0]] = count
        else:
            result_quantity = None

        return (result_revenue,result_quantity)


sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})

###
print(sales_stats([('Apple', 10, 0.5), ('Orange', 5, 0.6)], revenue = True, quantity = True))

"""
Ожидаемый ответ:
(8.0, {'Apple': 10, 'Orange': 5})
Ваш ответ:
(None, {'Apple': 10, 'Orange': 5})
"""


#Задание 19.7.3 (External resource)
print("\n---------------------------------------->\n")

"""
Отчет представляет собой строку, которая содержит информацию о среднем доходе и общем количестве проданных
единиц товара за определенный период. Функция должна принимать на вход данные о продажах (в том же формате, что и в задаче выше)
и функцию, которую нужно использовать для обработки этих данных (функция из предыдущей задачи).
"""

def create_report(dataList,function=sales_stats):
    #[(690, {'яблоки': 27, 'груши': 5})]
    data = function(dataList)
    resultStr = ''
    resultStr += f"Средний доход за данный период составил {data[0]/len(dataList)}."
    resultStr += "\nКоличество проданных единиц каждого товара:"

    for key,value in data[1].items():
        #print(f'{key}: {value}')
        resultStr += f"\n{key}: {value}"
    #print(resultStr)
    return resultStr
#--------------------------------------------------
def dummy_func(data, **kwargs):
    revenue = 100.0
    quantity = {"Apple": 10, "Orange": 5}
    return revenue, quantity
#--------------------------------------------------

sales_data = [["яблоки", 20, 20], ["груши", 5, 30], ["яблоки", 7, 20]]
print(create_report(sales_data, sales_stats))
# Средний доход за данный период составил 230.0.
# Количество проданных единиц каждого товара:
# яблоки: 27
# груши: 5

print(create_report([('Apple', 10, 0.5)], dummy_func))
#Средний доход за данный период составил 100.0.
#Количество проданных единиц каждого товара:
#Apple: 10
#Orange: 5

"""
Ожидаемый ответ:

Средний доход за данный период составил 50.0.
Количество проданных единиц каждого товара:
Apple: 10
Orange: 5

Ошибка:

Traceback (most recent call last):
  File "O3W1BO9C7OPZM88DZX6E.py", line 7, in <module>
    def create_report(dataList,function=sales_stats):
NameError: name 'sales_stats' is not defined

-----------------------------------------------------

def create_report(dataList,function=sales_stats):
    #[(690, {'яблоки': 27, 'груши': 5})]
    data = function(dataList,revenue=True,quantity=True)
    print(f"Средний доход за данный период составил {data[0]/len(dataList)}.")
    print("Количество проданных единиц каждого товара:")
    for key,value in data[1].items():
        print(f'{key}: {value}') 


Ожидаемый ответ:

Средний доход за данный период составил 100.0.
Количество проданных единиц каждого товара:
Apple: 10
Orange: 5

Ошибка:

Traceback (most recent call last):
  File "U36JFWCTU7MB4QAYNJ7A.py", line 7, in <module>
    def create_report(dataList,function=sales_stats):
NameError: name 'sales_stats' is not defined
"""

#Задание 19.7.4 (External resource)
print("\n---------------------------------------->\n")

"""
Напишите функцию sort_users_by_activity, которая будет возвращать список пользователей, отсортированных
по уровню активности в порядке убывания. Функция sorted должна использоваться с аргументом key и лямбда-функцией.
"""

def sort_users_by_activity(dect_users):
    sorted_users = dict(sorted(dect_users.items(), key=lambda item: item[1], reverse=True))
    return list(sorted_users.keys())

user_activity = {"user1": 10, "user2": 5, "user3": 20, "user4": 15, "user5": 10}
print(sort_users_by_activity(user_activity))
# ['user3', 'user4', 'user1', 'user5', 'user2']
