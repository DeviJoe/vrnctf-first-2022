FROM python:3.8-slim-buster
COPY .. /app
WORKDIR /app
RUN pip3 install Flask
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]