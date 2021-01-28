FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get install -qq -y ca-certificates curl gcc && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /app

RUN pip3 install --upgrade pip setuptools

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
