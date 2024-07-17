from channels.generic.websocket import WebsocketConsumer
from app.channels.dispatcher import dispatch


class OBSControlWebSocketConsumer(WebsocketConsumer):


    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        pass


    def receive(self, text_data):
        dispatch(self, text_data)
