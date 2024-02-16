from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class Test(WebsocketConsumer):
    def connect(self):
        self.room_name = "Test"
        self.room_group_name = "Test_Group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data= json.dumps({'message':'Connected'}) )

    def receive(self, text_data=None):
        print(text_data)
        self.send(text_data= json.dumps({'message':'Received Data','data':text_data}))
       
    def disconnect(self, close_code):
        print("Disconnected")