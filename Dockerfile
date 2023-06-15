FROM ubuntu:22.04
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip 
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app

CMD [ "python3", "./app.py"]