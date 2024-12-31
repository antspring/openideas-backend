FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
 
EXPOSE 8000

CMD ["sh", "-c", "python3 manage.py migrate && gunicorn openideas.wsgi:application --bind 0.0.0.0:8000"]