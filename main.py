from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
import aiocron

from dbhelper import DBHelper

#get your own api_id and api_hash from https://my.telegram.org, under API Development
api_id = 'API_ID'
api_hash = 'API_HASH'
string = 'STRING'
client = TelegramClient(StringSession(string), api_id, api_hash)
client.start()

db = DBHelper()

@aiocron.crontab("21 4 * * *", start = False) #set a cron job for sending Telegram message 
async def main():
    async with client:
        try:
            result = db.get_items()
            insta_url = result[0][0]
            caption = result[0][1]
            index = result[0][2]
            await client.send_message('TELEGRAM_ID', insta_url) #send an instagram post to user
            await client.send_message('TELEGRAM_ID', caption) #send a caption to user
            db.delete_item(index)
        except:
            await client.send_message('me', "Error") #send 'Error' message to yourself if the messages are not sent
            
main.start()
asyncio.get_event_loop().run_forever()
