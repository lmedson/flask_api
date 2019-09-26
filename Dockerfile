FROM python:3.7
COPY src/ .
WORKDIR /app
RUN pip install -r requeriments.txt
WORKDIR /src
RUN export flask db init
RUN flask db migrate
RUN flask db upgrade
ENTRYPOINT flask run