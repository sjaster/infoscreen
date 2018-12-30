FROM python:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements

EXPOSE 5000

CMD ["python", "/app/main.py"]
