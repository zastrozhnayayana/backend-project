# Backend Project

## Что умеет

- `GET /` — проверка, что сервер работает
- `GET /health` — healthcheck
- `GET /tasks` — получить список задач
- `POST /tasks` — добавить задачу
- `DELETE /tasks/{task_id}` — удалить задачу

Данные хранятся в памяти, без базы данных. После перезапуска сервера список задач очищается.

## Как запустить

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

После запуска открыть:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Пример запроса

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Build a backend project"}'
```
