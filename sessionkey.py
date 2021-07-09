from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = '5254120'
api_hash = 'aac1e1210276e4ed0a4e72cd9ffd6bde'
client = TelegramClient('anon', api_id, api_hash)

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
