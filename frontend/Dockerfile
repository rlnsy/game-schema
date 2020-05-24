# Stage 1 - the build process
FROM node:11 as build-deps
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY . ./
RUN yarn build

#Stage 2 - the production environment
FROM nginx:1.15-alpine
COPY --from=build-deps /app/dist /usr/share/nginx/html
COPY ./nginx.local.conf /etc/nginx/nginx.conf
RUN mkdir /etc/ssl/gmbx
EXPOSE 80
EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]
