[![Python application](https://github.com/bnarasimha/DiscordBot/actions/workflows/python-app.yml/badge.svg)](https://github.com/bnarasimha/DiscordBot/actions/workflows/python-app.yml)

## DiscordBot
A discord bot which can be installed to Discord servers and it can act as a helper to asnwer questions based on the data fed by us.

### Setting Up Virtual Environment
To setup the virtual environment run the below commands:
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
### Storing environment variables:
Create DISCORD_TOKEN from Discord developer portal and add it as environment variable
```
DISCORD_TOKEN= <>
```
### Prepare VectorDB
Change any links and data to be fed into Vector DB and execute below command to vectorize data into the DB 
```python store_documents.py```

Alternatively, create a linux service "store_documents" provided under scripts folder, on the linux machine and start the service.


### Running the application
1. Run app.py to run it as api application and test it via postman etc
2. Run web.py to run it as a gradio application and test by providing questions in the text prompt
3. Run bot.py to run it as a Discord Bot so that whenever a question is posted in Discord app, it will fetch answer from this app and respond with answers.

### Setup Linux machine to run application as a service to help with continuous deployments
Run scripts/new_system_startup.sh to make sure application has all necessary tools and libraries in new linux machine to start working properly
