FROM python:3.9

#RUN apt-get -y install libwebp
RUN pip install fastapi uvicorn numpy Pillow

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
