#Create initial folders needed
mkdir Documents
cd Documents
mkdir discordbot
mkdir chromadb

#Install python
alias python=python3
sudo apt-get update
sudo apt install python3.10-venv

#Install Docker
sudo snap install docker
sudo chmod 777 /var/run/docker.sock

#Run chromadb as docker container and mount host path for persistent storage 
docker run -d -p 8000:8000 -v /home/paperspace/Documents/chromadb:/chroma/chroma chromadb/chroma

#install necessary libabries for application functioning
cd /home/paperspace/Documents/discordbot
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

#provide writing rights to chromadb
cd /home/paperspace/Documents
sudo chmod 777 chromadb
cd chromadb
sudo chmod 777 chroma.sqlite3

#Crawl and store documents in chromadb
cd /home/paperspace/Documents/discordbot
python store_documents.py

#Install Ollama and pull Mistral model
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral

#Restart system for proper Cuda functionaing 

#Create a linux service
sudo systemctl start discordbot-gradioapp

#Enable service to run on system start
sudo systemctl enable discordbot-gradioapp


