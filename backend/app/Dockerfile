FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY backend/app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]