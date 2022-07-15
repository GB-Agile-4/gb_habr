## Проект "НеХабр"
## Командная разработка по методологии Agile:Scrum

Основные системные требования:

* Win 10
* Python 3.10
* PostgreSQL 14
* Django 4.0
* Зависимости из requirements.txt

### Установка:

1. Клонируем репозиторий:
```
git clone git@github.com:GB-Agile-4/gb_habr.git
```
2. Устанавливаем зависимости:
```
pip install -r {path_to_requirements}/requirements.txt
```
3. Устанавливаем PostgreSQL

4. Создаем базу данных
```
CREATE DATABASE gb_habr;
```
Создаем пользователя 
```     
CREATE USER myprojectuser WITH PASSWORD 'password';
```
Добавляем привилегии
```
GRANT ALL PRIVILEGES ON DATABASE gb_habr TO myprojectuser; 
```
Устанавливаем кодировку 'UTF8'
```
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
```
Устанавливаем уровень изоляции
```
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
```
Устанавливаем TIME ZONE
```
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
Для выхода вводим «\q».

5. Устанавливаем psycopg2
```
pip install psycopg2
```
6. Создаем суперпользователя
```
python manage.py createsuperuser
```
7. Делаем миграции
```
python manage.py makemigrations
python manage.py migrate
```

### Запуск:
```
python manage.py runserver
```