FROM python:3.13-slim

WORKDIR /backend

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 80
CMD ["flask", "run", "--port=80", "--debug"]