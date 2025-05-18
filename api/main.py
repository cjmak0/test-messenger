from fastapi import FastAPI
from .message_service import MessageHandlerService
from uuid import UUID

app = FastAPI()
message_handler_service = MessageHandlerService()


@app.get("/healthcheck")
async def root():
    return {
        "message_count": message_handler_service.get_messages_count(),
        "most_recent_message": message_handler_service.get_most_recent_message()
    }

@app.post("/messages/")
def new_message(text: str, sender: str):
    return message_handler_service.new_message(text, sender)

@app.get("/messages/")
def get_all_messages():
    return message_handler_service.get_all_messages()

@app.get("/messages/{id}")
def get_message(id: UUID):
    try:
        return message_handler_service.get_message(id)
    except KeyError:
        return None

@app.delete("/messages/{id}")
def delete_message(id: UUID):
    try:
        return message_handler_service.delete_message(id)
    except KeyError:
        return None