FROM node:15-buster-slim
RUN apt-get update && apt-get install -qq -y curl && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /app

COPY package.json yarn.lock /app/
RUN yarn install && yarn cache clean

COPY . /app

EXPOSE 3000
CMD ["yarn", "start"]
