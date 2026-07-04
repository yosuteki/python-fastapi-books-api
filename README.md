# FastAPI Books API

API для работы с категориями и книгами через FastAPI, SQLAlchemy и PostgreSQL.

## Запуск

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app/init_db.py
uvicorn app.main:app --reload
```

Проверка:

- `GET http://127.0.0.1:8000/health`
- Swagger UI: `http://127.0.0.1:8000/docs`
- `GET http://127.0.0.1:8000/books`
- `GET http://127.0.0.1:8000/books?category_id=1`

Скриншоты выполнения находятся в `examples/`.
