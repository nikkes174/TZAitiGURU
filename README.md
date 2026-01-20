# Документация проекта
Тестовое задание: REST API для управления заказами, товарами и отчётами.
Проект реализован с использованием FastAPI, SQLAlchemy (async), Alembic, Poetry, Docker и покрыт тестами.


### Технологический стек

**Backend**:
- Python 3.12

- FastAPI

- SQLAlchemy (Async ORM)

- Alembic — управление схемой БД

- PostgreSQL / SQLite (для теста)

- Poetry — управление зависимостями

- Pytest + pytest-asyncio

- Docker / Docker Compose

- CI (GitHub Actions)

- Black + Ruff


### Структура проекта
```bash
TZAitiGuru/
├── main.py                         # Точка входа FastAPI приложения
│                                   # Подключение роутеров, startup hook
│
├── config.py                       # Конфигурация проекта
│                                   # DATABASE_URL (через env)
│
├── db.py                           # Инициализация SQLAlchemy
│                                   # Async engine, session, Base, get_db
│
├── alembic/                        # Миграции БД (Alembic)
│   ├── env.py                      # Конфигурация Alembic (async → sync)
│   ├── README                      # Служебный файл Alembic
│   └── versions/                  # Версии миграций
│       ├── initial_tables.py       # Создание всех таблиц
│       └── add_indexes_for_reports.py # Индексы под отчёты
│
├── Category/                       # Категории товаров 
│   ├── __init__.py
│   ├── models.py                   # SQLAlchemy модель Category
│   ├── schemas.py                  # Pydantic схемы (Create, Read, Reports)
│   ├── crud.py                     # CRUD-операции с категориями
│   ├── service.py                  # Бизнес-логика + отчёт children-count
│   └── router.py                   # API эндпоинты 
│
├── Product/                        # Товары
│   ├── __init__.py
│   ├── models.py                   # ProductModel
│   ├── schemas.py                  # ProductCreate, ProductRead, TopProductReport
│   ├── crud.py                     # CRUD товаров
│   ├── service.py                  # Логика + отчёт top-5-last-month
│   └── router.py                   # API эндпоинты
│
├── Customer/                       # Покупатели
│   ├── __init__.py
│   ├── models.py                   # CustomerModel
│   ├── schemas.py                  # CustomerCreate / CustomerRead
│   ├── crud.py                     # CRUD покупателей
│   ├── service.py                  # Бизнес-логика
│   └── router.py                   # API эндпоинты 
│
├── Order/                          # Заказы
│   ├── __init__.py
│   ├── models.py                   # OrderModel, OrderItemModel
│   ├── schemas.py                  # OrderCreate, OrderRead, OrderTotalByCustomer
│   ├── crud.py                     # CRUD заказов
│   ├── service.py                  # Добавление товаров + отчёты
│   └── router.py                   # API эндпоинты 
│
├── tests/                          # Тесты (pytest + httpx + sqlite)
│   ├── conftest.py                 # Фикстуры: test DB, app, client
│   ├── test_categories.py          # Тесты категорий и иерархии
│   ├── test_products.py            # Тесты товаров
│   ├── test_customers.py           # Тесты покупателей
│   ├── test_orders.py              # Тесты заказов и добавления товаров
│   └── test_reports.py             # Тесты отчётов
│
├── .github/
│   └── workflows/
│       └── ci.yml                  # CI: Ruff, Black, Pytest
│
├── pyproject.toml                  # Poetry конфигурация
├── poetry.lock                     # Зафиксированные зависимости
├── Dockerfile                      # Docker-образ приложения
├── docker-compose.yml              # App + PostgreSQL
├── README.md                       # Описание проекта и запуск```

### Инструкция по запуску

Запуск через Docker
```bash
docker compose up --build
```

### Тесты
```bash
poetry run pytest -v
```

### Миграции (Alembic)
Создание новой миграции:
```bash
poetry run alembic revision -m "migration_name"
```
Применение:
```bash
poetry run alembic upgrade head
```

### Реализованные отчёты

Количество дочерних категорий
```bash
GET /categories/reports/children-count
```
Общая сумма заказов по клиентам
```bash
GET /orders/reports/total-by-customers
```

ТОП-5 товаров за последний месяц
```bash
GET /products/reports/top-5-last-month
```

### CI
В проекте настроен GitHub Actions:

- ruff — линтинг

- black — проверка форматирования

- pytest — прогон тестов

CI запускается на каждый push и pull request.