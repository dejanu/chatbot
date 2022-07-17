# python base image
FROM python:3.8-slim

# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
# COPY datasets ./datasets
RUN mkdir datasets
COPY second_chatbot.py corpusreader.py .
VOLUME /app/datasets

ENTRYPOINT ["python","./second_chatbot.py"]