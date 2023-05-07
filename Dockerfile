FROM python:3.10.10-slim-buster

WORKDIR /app
COPY requirements.txt /app
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
RUN apt-get install libpq-dev

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]