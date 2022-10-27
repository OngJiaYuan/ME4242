import json
from channels.generic.websocket import WebsocketConsumer

class Controller(WebsocketConsumer):
    def connect(self):
        print('connection')
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connected',
            'message':'you'
        }))
    

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
