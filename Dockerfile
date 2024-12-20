FROM python:3.12.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
 
EXPOSE 8000

CMD ["gunicorn", "openideas.wsgi:application", "--bind", "0.0.0.0:8000"]