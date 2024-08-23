FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install git -y && apt-get install curl -y

RUN curl -fsSL https://ollama.com/install.sh | sh

RUN ollama serve &

RUN ollama pull mistral

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["python", "web.py"]