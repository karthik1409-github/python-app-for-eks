FROM python:3.8-slim-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY ./app.py /app
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]