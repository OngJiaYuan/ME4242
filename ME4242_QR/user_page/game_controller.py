import json
from channels.generic.websocket import WebsocketConsumer
from ME4242_Cover_Control.Cover_control import move

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
        print(move)
