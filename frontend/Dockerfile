# Sử dụng Nginx bản Alpine (cực nhẹ, chạy trên RAM rất ít)
FROM nginx:alpine

# Copy code của bạn đè lên thư mục mặc định của Nginx
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

# Mở cổng 80 bên trong container
EXPOSE 80