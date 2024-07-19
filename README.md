<p align="center"><img src="https://i.ibb.co/rcp4mz4/Group-7.png" alt="Main-logo" border="0" width="500"></p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.11-orange)" alt="Aiogram Version">
   <img src="https://img.shields.io/badge/Django-5.0.7-E86F00" alt="Aiohttp Version">
</p>

<p>WEB - приложение предоставляет возможность получить прогноз погоды на неделю, для любого города.</p>


## Описание работы
В поле вводим название города, для которого хотим получить прогноз погоды.<br>
Название города можно вводить на русском или английском языке.
Нажимаем кнопку "получить прогноз" или Enter для получения прогноза.
Кнопка "X" очищает поле ввода.

<p align="center">
<a href="https://i.ibb.co/Lk3k6jX/2024-07-19-16-22-11.png"><img src="https://i.ibb.co/Lk3k6jX/2024-07-19-16-22-11.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>


## Установка

Скачайте код:
```sh
git clone https://github.com/SwedL/weather.git
```
Перейдите в каталог проекта `weather`, создайте виртуальное окружение, выполнив команду:

- Windows: `python -m venv venv`
- Linux: `python3 -m venv venv`

Активируйте его командой:

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:

```sh
pip install -r requirements.txt
```

Запустите сервер:
```sh
python manage.py runserver
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

## Как запустить версию сайта в docker.
Скачайте код:
```sh
git clone https://github.com/SwedL/weather.git
```
Затем выполните сборку и запуск образа командами:
```sh
docker build . --tag weather
```
```sh
docker run --rm -d --publish 8000:8000 weather
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/">http://127.0.0.1:8000/</a>

### Тестирование

Проект покрыт тестами форм, представлений, URL, проверяющими его работоспособность.<br>
Тесты запускаются командой:
```sh
python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)

