from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import asyncio
import aiocron
import datetime

# https://pure-retreat-22528.herokuapp.com/
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = '5254120'
api_hash = 'aac1e1210276e4ed0a4e72cd9ffd6bde'
string = '1BVtsOK8BuxC33bZfBuoEb7Sc7PcreCej5SIA3RzDHIugAqZ3AEcXAwiJetHlAFLdBboV1XjX7bMZSvhVBXc7vCU6uEo_sjUq6ifd0R8CQ_vF5bHTpkc6fMok5LBe71ITgOVoStPDurJIzS1L9iM8GrbsPLjEc50wRhhT_coLxWwcuIqy2GsoysffBXnzIZ-KiYsHuF2cPuj5l1La0KPM4OfLxPwk_eMWt8vJaLqQnOAPitxOGQuBoAu3GoJA7cBnr9pWAA79fF4tZjENz21oKpgHog0SMBJgVSLTrmow0Pltpbdb2TxNwJ0vB479gfOf0czaoObXpGeirGgmjYGW2KgTSnkR-lE='
client = TelegramClient(StringSession(string), api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...

with client:
    client.loop.run_until_complete(main())
