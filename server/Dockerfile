FROM nginx:1.15-alpine
COPY ./static /usr/share/nginx/static
COPY ./media /usr/share/nginx/media
COPY ./nginx.local.conf /etc/nginx/nginx.conf
COPY ./uwsgi_params /uwsgi_params
#COPY ./ssl/gmbx.xyz.crt /etc/nginx/gmbx.xyz.crt
#COPY ./ssl/gmbx.xyz.key /etc/nginx/gmbx.xyz.key
CMD ["nginx", "-g", "daemon off;"]