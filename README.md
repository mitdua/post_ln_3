# FastAPI Redis Cache Example

This project is a simple FastAPI application that demonstrates the use of Redis for caching responses. It consists of two main endpoints: one without caching and one with Redis caching, both simulating a time-consuming process.

## Overview

The application provides two GET endpoints that simulate a slow response:

1. **`/no-cache`**: This endpoint simulates a slow process and returns the response without using any caching mechanism. This means that every request to this endpoint will result in the same process being repeated, which can lead to increased processing time.

2. **`/cache-redis`**: This endpoint also simulates a slow process, but utilizes Redis to cache the response for a certain period (60 seconds). This significantly speeds up subsequent requests, as the result is fetched from the cache instead of repeating the slow process.

## How It Works

- The **slow process** is simulated by making the server sleep for a random period between 3 to 6 seconds.
- For the `/cache-redis` endpoint, Redis is used to store the response so that repeated requests within the cache expiry time can be handled quickly.
- The response from the slow process is cached for **60 seconds**, after which it is recalculated.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.12+.
- **Redis**: An in-memory key-value store used for caching the responses.
- **Python 3.12+**: The programming language used for this project.

## Requirements

- **Docker** (Optional): To run both the FastAPI application and Redis using Docker.
- **Python 3.12+**: If running the project locally without Docker.

## Running the Project

You can run the project either with Docker or directly on your local machine.

### Running with Docker

To run the project with Docker:

1. Clone the repository:
    ```sh
    git clone https://github.com/mitdua/post_ln_3
    cd post_ln_3
    ```

2. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

This command will start both the FastAPI server and a Redis instance.


## Endpoints

- **`GET /no-cache`**: Returns the result of a slow process without caching.
- **`GET /cache-redis`**: Returns the result of a slow process, using Redis to cache the response for faster subsequent retrieval.

## Example Usage

You can use tools like **cURL** or **Postman** to interact with the API:

- To make a request to the non-cache endpoint:
  ```sh
    time curl -X POST http://localhost:8000/no-cache
  ```

  ```sh
    time curl -X POST http://localhost:8000/cache-redis
  ```