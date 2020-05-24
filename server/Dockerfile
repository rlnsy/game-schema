FROM nginx:1.15-alpine
COPY ./static /usr/share/nginx/static
COPY ./media /usr/share/nginx/media
COPY ./nginx.local.conf /etc/nginx/nginx.conf
COPY ./uwsgi_params /uwsgi_params
RUN mkdir /etc/ssl/gmbx
CMD ["nginx", "-g", "daemon off;"]