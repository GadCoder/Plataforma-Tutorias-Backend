import os
import pika
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from adapters.controllers.base import api_router

load_dotenv()

RABBITMQ_URL = os.environ.get("RABBITMQ_URL")

app = FastAPI()

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_URL)) # add container name in docker
channel = connection.channel()
channel.queue_declare(queue='gatewayservice')

app.include_router(api_router, prefix="/api/v1/gateway")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)