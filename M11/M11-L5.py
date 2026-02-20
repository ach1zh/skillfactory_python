#M11-L5

# Задание 22.4

"""
isbn (уникальный идентификатор книги);
title (название книги);
author (автор книги);
year (год выпуска книги).
status available/not available
"""

class LibrarySystem:

    def __init__(self):
        
        self.book_store = dict()
        # Ключом словаря будет уникальный идентификатор книги (ISBN), 
        # а значением будет вложенный словарь, содержащий информацию о книге (название, автор, год выпуска, статус).

    def add_book(self,isbn,title,author,year,status="Available"):        
        self.book_store[isbn] = {"title":title,"author":author,"year":year,"status":status}
        #self.book_store.update({isbn:{"title":title,"author":author,"year":year,"status":status}})

    def change_status(self,isbn,status):
        self.book_store[isbn]["status"] = status

    def search_book(self,isbn):
        #Выводит информацию о книге (название, автор, год выпуска, статус) или сообщение о том, что книга с таким ISBN не найдена.
        if self.book_store.get(isbn):
            print("Название: " + self.book_store[isbn]["title"])
            print("Автор: " + self.book_store[isbn]["author"])
            print("Год выпуска: " + self.book_store[isbn]["year"])
            print("Статус: " + self.book_store[isbn]["status"])
        else:
            print("Книга с таким ISBN не найдена")    

print("\n-->")

library_system = LibrarySystem()

isbn1 = "978-5-389-12345-6"
title1 = "Мастер и Маргарита"
author1 = "Михаил Булгаков"
year1 = "2023"

isbn2 = "978-5-17-098765-4"
title2 = "Преступление и наказание"
author2 = "Фёдор Достоевский"
year2 = "2022"

isbn3 = "978-5-04-112389-1"
title3 = "451° по Фаренгейту"
author3 = "Рэй Брэдбери"
year3 = "2024"

library_system.add_book(isbn1, title1, author1, year1)
library_system.add_book(isbn2, title2, author2, year2)
library_system.add_book(isbn3, title3, author3, year3)


#print(library_system.__dict__)
library_system.change_status(isbn2,'Not available')
#print(library_system.__dict__)
library_system.search_book(isbn3)

"""
ДОП
Чтобы убедиться в эффективности использовании хеш-таблиц на практике, попробуйте решить эту задачу без их использования, например,
храните информацию о книгах просто как список. Затем сгенерируйте большое количество фиктивных данных или добудьте их в открытом доступе
и сравните скорость работы двух реализаций — с использованием словарей и без.
"""