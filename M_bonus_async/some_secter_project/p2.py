from aiohttp import web

app = web.Application()
#прописываем роуты (похоже на Django)
app.add_routes([web.get('/', index)] )

if __name__ == '__main__':
   web.run_app(app)


   # создаём веб-приложение, которое работает в асинхронном режиме
app = web.Application()
# задаём движку шаблонов папку, из которой он будет брать шаблоны
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str('.\templates')))

#прописываем роуты
app.add_routes([web.get('/', index)])

#запускаем наше асинхронное веб-приложение
if __name__ == '__main__':
   web.run_app(app)