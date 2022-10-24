FROM node:lts-alpine

ENV DockerHOME=/web

# make the 'app' folder the current working directory
WORKDIR $DockerHOME

# install simple http server for serving static content
RUN yarn add http-server

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN yarn install

# copy project files and folders to the current working directory (i.e. 'web' folder)
COPY . .

# build app for production with minification
RUN yarn build

EXPOSE 8080
CMD [ "http-server", "dist" ]