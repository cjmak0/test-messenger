from typing import Dict
from .message import Message
from uuid import uuid4, UUID

class MessageHandlerService():
    def __init__(self):
        self.messages: Dict[UUID, Message] = {}
        self.most_recent_id: UUID

    def new_message(self, text: str, sender: str) -> UUID:
        new_id = uuid4()
        self.messages[new_id] = Message(
            id=new_id, 
            message=text, 
            sender=sender)
        return new_id
    
    def delete_message(self, id: UUID):
        if id in self.messages:
            self.messages.pop(id)
        else:
            raise KeyError(f"Key of {id} not present in messages")
    
    def get_message(self, id: UUID) -> Message:
        if id in self.messages:
            return self.messages[id]
        else:
            raise KeyError(f"Key of {id} not present in messages")

    def get_all_messages(self) -> Dict[str, Message]:
        return self.messages
    
    def get_messages_count(self) -> UUID:
        return len(self.messages)
    
    def get_most_recent_message(self) -> Message:
        if len(self.messages) == 0:
            return None
        
        recent_key = list(self.messages.keys())[-1]
        if self.messages[recent_key]:
            return self.messages[recent_key]
        else:
            return None

        