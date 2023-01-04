
# TODO: Выполненный проект должен сопровождаться описанием 
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```
Обновить версию pip
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
pip freeze > requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
При необходимости создать суперпользователя:
```
python manage.py createsuperuser
```
Запустить проект:
```
python3 manage.py runserver
```

