# Запуск
1. Клонирование репозитория
```bash
https://github.com/ggerlakh/fastapi-app-example.git && cd fastapi-app-example
```
2. Установка зависимостей
```bash
pip3.11 install -r app/requirements.txt
```
3. Запуск приложения через `uvicorn`
```bash
uvicorn app.main:app
```