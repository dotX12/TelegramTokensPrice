import time


class AntiFloodRate:
    def __init__(self, client):
        self.msg_list = []
        self.client = client

    async def delete_my_messages(self):
        current_time = time.time()
        for index, msg in enumerate(self.msg_list):
            if current_time >= msg['delete_time']:
                await self.client.delete_messages(msg['data']['chat_id'], msg['data']['msg_id'])
                del self.msg_list[index]
