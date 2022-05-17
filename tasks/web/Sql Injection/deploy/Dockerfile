FROM python:3.8-slim-buster
COPY app /app
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app

CMD [ "python3", "app.py"]
