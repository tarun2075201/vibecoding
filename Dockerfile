FROM python:3.10-slim

WORKDIR /app

COPY backend /app/backend

RUN pip install fastapi uvicorn pyyaml croniter

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
