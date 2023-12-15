# Catalog of products

## Description

---

Simple API for Catalog System written with Python using FastAPI, SQL Alchemy and PostgreSQL.

### Construction 🛠️

- **Language:** Python 3
- **Framework:** FastAPI, SQL Alchemy
- **Database:** PostgreSQL

### Architecture

The proposed architecture aims to decouple the system into simple layers, with a primary focus on separating responsibilities to maintain code reusability. An improvement or evolution of this architecture would be the "hexagonal architecture," comprising three fundamental layers: the Application layer, the Domain layer, and the Infrastructure layer. In this context, the repository and service layers used in the project can significantly ease the transition to this architecture in case business requirements undergo changes or evolution.

---

## Requirements

---

- Docker installed

## Installation and execution

---

Clone or Fork the project.

Run `docker-compose` command inside **docker-python** folder.

- Building the containers: `docker-compose build`

- Starting the services: `docker-compose up -d`

- Stoping the services: `docker-compose stop`

By default the microservice will run under the following port:

- my_store_service: 8000

## Documentation

---

The detailed API Documentation is available on the endpoint `http://localhost:8000/redoc`\
For somes tests you can also visit `http://localhost:8000/docs`

<!-- ### Making a request

To make a request for all the store's products & users you would do the following in curl:

```curl
curl -H 'Authorization: Bearer ACCESS_TOKEN ' \
  http://localhost:8000/products/5
```

where `ACCESS_TOKEN` is the store's access token (see Authentication).

### Authentication

This project follow the OAuth2 framework for letting users authorize use endpoints

To get the access token you need to run the following curl:

```curl
curl --request POST \
  --url http://localhost:8000/token \
  --header 'Content-Type: multipart/form-data;' \
  --form username=admin@example.com \
  --form password=string \
  --form grant_type=password
``` -->

#### Note 🔍

The endpoint `POST /users` for create users was intentionally left freely accessible so that the first admin user can be created

### Author ✒️

- **Raul Vidal**
