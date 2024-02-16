from channels.generic.websocket import AsyncWebsocketConsumer
import json, time, random,asyncio
from faker import Faker
from channels.layers import get_channel_layer

class StudentInfo(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'StudentInfo'
        self.room_group_name = 'studentinfo_group'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status':'Connected'}))

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = text_data
        await self.send(text_data=json.dumps({'message':data+' received'}))
        data=int(data)
        for i in range(data):
            student_info = generate_student_info()
            await self.send(text_data=json.dumps({'status':'connected','id':i+1,'studentinfo':student_info}))
            await asyncio.sleep(0.1)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.send(text_data=json.dumps({'status':'Disconnected'}))

# Generate 10 random student information
def generate_student_info():
    fake = Faker()
    student_name = fake.name()
    student_address = fake.address()
    faculties = ["Engineering", "Science", "Arts", "Commerce", "Medical"]
    student_faculty = random.choice(faculties)
    return {
        "student_name": student_name,
        "student_address": student_address,
        "student_faculty": student_faculty
    }
