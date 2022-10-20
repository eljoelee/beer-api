FROM python:3.10

COPY . /app/server

WORKDIR /app/server

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python", "./main.py"]