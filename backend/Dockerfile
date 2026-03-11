FROM python:3.13-slim

WORKDIR /backend

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY . .

# 2. Cài đặt thư viện (Layer này sẽ được lưu cache, không cài lại nếu file requirements không đổi)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 3. Sau đó mới Copy toàn bộ code vào


EXPOSE 80
CMD ["flask", "run", "--port=80", "--debug"]