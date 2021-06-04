FROM python:3.7.6-buster

COPY ./env/requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app/src/
EXPOSE 8005

COPY ./app/app.py .
CMD ["python3","./app.py"]