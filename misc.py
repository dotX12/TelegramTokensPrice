from telethon import TelegramClient
import env_load
from storage import AntiFloodRate
from utils import Math, WrapperJson

from dotenv import load_dotenv
import os
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')

client = TelegramClient("session", api_id, api_hash)
client.start()
flood = AntiFloodRate(client)
math = Math()
wrapper = WrapperJson()
