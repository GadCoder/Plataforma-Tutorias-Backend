import pika
import uvicorn
from fastapi import FastAPI
from adapters.controllers.router import api_router


connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()
channel.queue_declare(queue='auth_service')

app = FastAPI()
app.include_router(api_router, prefix="/api/v1/auth")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)