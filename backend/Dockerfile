FROM python:3.14.0b2-alpine3.22

WORKDIR app

EXPOSE 8000

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

RUN rm -f requirements.txt

CMD [ "python", "app.py" ]