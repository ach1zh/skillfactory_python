# загружаем класс для работы с web
from aiohttp import web
# загружаем движок для работы с шаблонами
import aiohttp_jinja2
import jinja2

#при помощи декоратора указываем, какой файл шаблона будет использоваться в связке с этой корутиной
@aiohttp_jinja2.template('index.html')
async def index(request):
   # текст задач для подстановки в шаблон можно брать из БД, файла или генерировать на лету
   tasks = []
   tasks.append({"task_text":"task 1: prepare breakfast"})
   tasks.append({"task_text":"task 2: do SF task"})
   tasks.append({"task_text":"task 3: take a walk"})
   tasks.append({"task_text":"task 4: go to bed on time"})
   return {"tasks": tasks}
  

# создаём веб-приложение, которое работает в асинхронном режиме
app = web.Application()
# задаём движку шаблонов папку, из которой он будет брать шаблоны
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str('.\templates')))

#прописываем роуты
app.add_routes([web.get('/', index)])

#запускаем наше асинхронное веб-приложение
if __name__ == '__main__':
   web.run_app(app)