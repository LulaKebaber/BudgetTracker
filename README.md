# Budget Tracker

Djanngo Rest Framework API for saving your expenses and debts

## Technologies

- Django
- Django Rest Framework
- PostgreSQL
- Docker

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/LulaKebaber/BudgetTracker

2. Create venv:
   
   ```bash
   python -m venv venv
   source venv/bin/activate

3. Install requirements:

   ```bash
   pip install -r requirements.txt

4. Create .env file and add DB_NAME, DB_USER, DB_PASSWORD, DB_HOST and DJANGO_SECRET_KEY variables

4. Run project:

   ```bash
   docker-compose build
   docker-compose up -d
   docker-compose logs -f

## Endpoints API

| №  | Эндпоинт                  | Метод | Описание                                 |
|----|---------------------------|-------|------------------------------------------|
| 1  | `/add-expense/`           | POST  | Создание нового расхода                 |
| 2  | `/add-house-member/`      | POST  | Добавление нового участника дома        |
| 3  | `/add-person/`            | POST  | Добавление новой персоны                |
| 4  | `/add-settlement/`        | POST  | Добавление нового расчета               |
| 5  | `/create-house/`          | POST  | Создание нового дома                    |
| 6  | `/get-debt/{telegram_id}/`| GET   | Получение информации о задолженности    |
| 7  | `/get-house-info/{house_name}/` | GET   | Получение информации о доме         |