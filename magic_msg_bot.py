from fbchat import Client
from fbchat.models import *

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        # If you're not the author, echo
        if author_id != self.uid:
            if message_object.text.lower() == 'ke ho bhan':
                self.sendLocalImage(
                                "FOH.png",
                                thread_id=thread_id,
                                thread_type=thread_type,
                                )
                self.send(Message(text="😂😂😂", emoji_size=EmojiSize.LARGE), thread_id=thread_id, thread_type=thread_type)
            elif message_object.text.lower() == 'feri bhan':
                self.sendLocalImage(
                                "NOC.jpg",
                                thread_id=thread_id,
                                thread_type=thread_type,
                                )
                self.send(Message(text="😆😆😆", emoji_size=EmojiSize.LARGE), thread_id=thread_id, thread_type=thread_type)
            

client = EchoBot("aaryan.dhakal22@gmail.com", "aarebdhakal")
client.listen()