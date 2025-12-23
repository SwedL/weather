<p align="center"><img src="https://i.ibb.co/rcp4mz4/Group-7.png" alt="Main-logo" border="0" width="500"></p>

<p align="center">
   <img src="https://img.shields.io/badge/Python-3.11-orange)" alt="Aiogram Version">
   <img src="https://img.shields.io/badge/Django-5.0.7-E86F00" alt="Aiohttp Version">
</p>

<p>WEB - приложение предоставляет возможность получить прогноз погоды на неделю, для любого города.</p>


## Описание работы
В поле вводим название города, для которого хотим получить прогноз погоды.<br>
Название города можно вводить на русском или английском языке.<br>
Нажимаем кнопку "получить прогноз" или Enter для получения прогноза.<br>
Кнопка "X" очищает поле ввода.

<p align="center">
<a href="https://i.ibb.co/Lk3k6jX/2024-07-19-16-22-11.png"><img src="https://i.ibb.co/Lk3k6jX/2024-07-19-16-22-11.png" alt="2024-03-08-14-02-52" border="0"></a>
</p>


## Установка

- ### Склонируйте репозиторий:
```sh
git clone https://github.com/SwedL/weather.git
cd weather
```
- ### Создайте и активируйте виртуальное окружение:
- #### через pip:
```
python -m venv venv
.\venv\Scripts\activate
```

- установите зависимости в виртуальное окружение:

```sh
pip install -r requirements.txt
```

- #### через Poetry:
```sh
poetry shell
poetry install
```

- ### Создайте необходимые таблицы базы данных командой:
```sh
python manage.py migrate
```

- ### Запустите сервер:
```sh
python manage.py runserver
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>

## Как запустить версию сайта в docker.
- ### Склонируйте репозиторий:
```sh
git clone https://github.com/SwedL/weather.git
cd weather
```
- ### Выполните сборку и запуск образа командами:
```sh
docker build . --tag weather
```
```sh
docker run --rm -d --publish 8000:8000 weather
```
Сервер работает на адресе <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>

### Тестирование

Проект покрыт тестами форм, представлений, URL, проверяющими его работоспособность.<br>
Тесты запускаются командой:
```sh
python manage.py test
```
## Автор проекта

* **Осминин Алексей** - [SwedL](https://github.com/SwedL)

