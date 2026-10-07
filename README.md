# Task Manager

Простое веб-приложение для управления задачами.

## Структура проекта

- `src/main.py` — точка входа приложения.
- `src/models.py` — модели данных.
- `src/utils.py` — вспомогательные функции.
- `tests/test_main.py` — автоматические тесты.


## Технологии

- Python
- Flask
- pytest
- Project B Utility Library

## Возможности

- просмотр списка задач;
- добавление задач;
- выполнение задач;
- удаление задач;
- сохранение задач в JSON;
- автоматическое отображение текущей даты;
- логирование операций.

## Установка

Клонировать репозиторий:
```
git clone https://github.com/JustANormalThing/project-a
```

## Запуск

If you want to download one lib use this
```
py -m pip install -r requirements.txt
```
py -m pip install  requirements.txt

```bash
python -m src.main
pytest tests/   
py app.py
