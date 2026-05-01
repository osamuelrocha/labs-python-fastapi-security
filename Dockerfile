FROM python:3.14-slim

WORKDIR /app

COPY src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

ENV PYTHONPATH=/app/src

EXPOSE 8001 8002

CMD ["uvicorn", "auth_api.main:app", "--host", "0.0.0.0", "--port", "8001"]
