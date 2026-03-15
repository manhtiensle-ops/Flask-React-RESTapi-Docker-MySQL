FROM nginx:alpine
WORKDIR /webapp

COPY ./public /usr/share/nginx/html/

COPY ./root ./admin

COPY ./default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
