from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
import aiocron
import datetime

from dbhelper import DBHelper
# https://pure-retreat-22528.herokuapp.com/
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = '5254120'
api_hash = 'aac1e1210276e4ed0a4e72cd9ffd6bde'
string = '1BVtsOK8BuxC33bZfBuoEb7Sc7PcreCej5SIA3RzDHIugAqZ3AEcXAwiJetHlAFLdBboV1XjX7bMZSvhVBXc7vCU6uEo_sjUq6ifd0R8CQ_vF5bHTpkc6fMok5LBe71ITgOVoStPDurJIzS1L9iM8GrbsPLjEc50wRhhT_coLxWwcuIqy2GsoysffBXnzIZ-KiYsHuF2cPuj5l1La0KPM4OfLxPwk_eMWt8vJaLqQnOAPitxOGQuBoAu3GoJA7cBnr9pWAA79fF4tZjENz21oKpgHog0SMBJgVSLTrmow0Pltpbdb2TxNwJ0vB479gfOf0czaoObXpGeirGgmjYGW2KgTSnkR-lE='
client = TelegramClient(StringSession(string), api_id, api_hash)
client.start()

db = DBHelper()

@aiocron.crontab("21 4 * * *", start = False)
async def main():
    async with client:
        try:
            time = datetime.datetime.today().strftime("%H.%M")
            result = db.get_items()
            insta_url = result[0][0]
            caption = result[0][1]
            index = result[0][2]
            print(index)
            print(insta_url)
            print(caption)
            print(time)
            await client.send_message(13749979, insta_url) #send insta to singyi
            await client.send_message(13749979, caption) #send caption to singyi
            db.delete_item(index)
        except:
            await client.send_message('me', "error bro")
main.start()
#asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
