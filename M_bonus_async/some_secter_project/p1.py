# загружаем класс для работы с web
from aiohttp import web

#обработчик для страницы по умолчанию
async def index(request):
# html-код формы мы поместили в templates  
   return web.FileResponse('M:\YandexDisk\-Sync-\Dev\python_projects\skillfactory_python\M_bonus_async\some_secter_project\templates\index.html')


#обработчик метода post, который посылается серверу при отправке формы
async def process_login_form(request):
   data = await request.post()
#получаем данные формы
   login = data['login']
   password = data['password']
#возвращаем ответ 
   return web.Response(text=f'your login is {login} your password is {password}')

#создаём веб-приложение, которое работает в асинхронном режиме
app = web.Application()
#прописываем роуты
app.add_routes([web.get('/', index)
              ,web.post('/login', process_login_form)] )

#запускаем наше асинхронное веб-приложение
if __name__ == '__main__':
   web.run_app(app)