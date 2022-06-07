FROM python:3.10-buster

WORKDIR /app

COPY /requirements/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]