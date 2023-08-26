import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        order_id = text_data_json['order_id']
        new_status = text_data_json['new_status']

    
        await self.send(text_data=json.dumps({
            'order_id': order_id,
            'new_status': new_status,
        }))
