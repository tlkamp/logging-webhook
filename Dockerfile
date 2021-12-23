FROM python:3

RUN pip install flask

WORKDIR /app
COPY main.py /app/

ENTRYPOINT [ "python", "main.py"]