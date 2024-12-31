# Openideas API

## Requirements

- Python 3.12

## Installation and running

### Clone the repository:
```bash
git clone https://github.com/antspring/openideas-backend.git
```

### Go to directory

```bash
cd openideas-backend
```

### Copy the .env file from .env.example and fill it out
```bash
cp .env.example .env
```

### Set up and run database

### Run the application with Docker

```bash
docker-compose up --build
```

### Run the application without Docker

```bash
pip install requirements.txt
```

```bash
python3 manage.py runserver
```

### Launch migrations without Docker

```bash
python3 manage.py migrate
```

### Create superuser

```bash
python3 manage.py createsuperuser
```