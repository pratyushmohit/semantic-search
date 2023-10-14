# FastAPI Semantic Search with Qdrant Vector Database

This repository contains a FastAPI-based web application that enables semantic search using a Qdrant Vector Database. The application provides endpoints for uploading text data, generating embeddings, and finding similar sentences.

## Installation and Setup
1. Clone this repository to your local machine.
2. Run `make build` command to build the docker image.
3. Once the image is built, run `make up-dev` to start the containers. You should be able to access the application on `http://0.0.0.0:8000`.
4. Import the collections json file in the Postman Collections directory onto Postman.
5. Start playing around!

Please ensure that you have a Qdrant Vector Database instance running and accessible for this application to work as intended.

## Author
- Pratyush Mohit

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Feel free to customize this README to include additional information, contact details, and license terms as needed for your project.