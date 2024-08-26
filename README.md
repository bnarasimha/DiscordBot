[![Python application](https://github.com/bnarasimha/DiscordBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/bnarasimha/DiscordBot/actions/workflows/python-app.yml)

## DiscordBot
A discord bot which can be installed to Discord servers and it can act as a helper to asnwer questions based on the data fed by us.

### Running the application

1. docker-compose.yml file is available in project root directory.
2. ```docker compose up``` command should spin up 3 containers.
    a. ChromaDB container
    b. Store documents container which executes store_documents.py and stores the Documents in ChromaDB
    c. Webapp container which is a Gradio app providing Q&A feature to the users
