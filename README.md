# Semantic Search: FastAPI, Celery, Redis and Qdrant

A FastAPI-based web application that enables semantic search using a Qdrant Vector Database. It uses Celery workers with a Redis broker to handle background tasks i.e, generating embedding and upserting to vector database. The application provides endpoints for uploading text data, generating embeddings, getting status of the upload and finding similar sentences.

This repository provides a Docker Compose configuration for setting up a semantic search application with multiple services. The application consists of the following components:

- `semantic-search`: A FastAPI application for semantic search.
- `celery-worker`: A Celery worker for background processing.
- `qdrant`: A Qdrant Vector Database server for vector search.
- `redis`: A Redis instance for message queuing and caching.


## Installation and Setup
1. Clone this repository to your local machine.
2. Run `make build` command to build the docker images for FastAPI Semantic Search and Celery Worker.
3. Once the images are built, run `make up-dev` to start all the containers. You should be able to access the application on `http://0.0.0.0:8000`.
4. Import the collections json file in the Postman Collections directory onto Postman.
5. Start playing around!

## Author
- Pratyush Mohit

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Feel free to customize this README to include additional information, contact details, and license terms as needed for your project.