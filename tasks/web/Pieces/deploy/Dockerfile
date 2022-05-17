FROM nginx:1.16.0-alpine

RUN rm -v /etc/nginx/conf.d/default.conf
ADD default.conf /etc/nginx/conf.d/
COPY . /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]
