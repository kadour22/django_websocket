from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("🔌 WebSocket connect called")
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()
        print("✅ WebSocket connected")

    async def disconnect(self, close_code):
        print(f"❌ WebSocket disconnected: {close_code}")
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        message = event["message"]
        print(f"📨 Sending notification: {message}")
        await self.send(text_data=json.dumps({
            "type": "notification",
            "message": message
        }))
