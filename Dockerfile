FROM python:3.13.12-slim

WORKDIR /webservice

RUN pip install update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python /backend/main.py

COPY . .

CMD [ "python3", "./backend/main.py"]