FROM python:3.10-slim-buster

WORKDIR /url-shortener

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["run.py"]
