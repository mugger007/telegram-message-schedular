from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = "API_ID"
api_hash = "API_HASH"
client = TelegramClient('anon', api_id, api_hash)

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())
