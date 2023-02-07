import asyncio
from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import InputPeerChannel
from telethon.sessions import StringSession
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import json


async def get_channel_messages(chat_id, msg_id):
    # Telegram API ID and Hash (you can get it from my.telegram.org)
    api_id = 'xxxxxxxx'
    api_hash = 'xxxxxxxxxxxxxx'
    session_hash='0KSDgh9xxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxx1dfsHNVugzasdHRShvewqWla889BH='
    # Identify your bot with his ID number, can be found using this link
    my_bot_id = 'xxxxxxxxx_my-bot-id-number_xxxxxxxx'
    # Storing max 3 past messages
    max_memory_message = 3

    chat_id = int(chat_id)
    data = {}
    # Create a Telegram client with the given session string
    async with TelegramClient(StringSession(session_hash), api_id, api_hash) as client:
        # Connect to Telegram
        await client.connect()

        # Get the channel by its username
        channel = await client.get_entity(PeerChannel(chat_id))
        messages = await client.get_messages(channel, limit=100, offset_id=0)

        for x in messages:
            try:
                if x.text != "":
                    if x.text is not None:
                        try:
                            replied = x.reply_to.reply_to_msg_id
                        except:
                            replied = x.reply_to
                        # The code stores the following information for each message in a dictionary: message id, date, user id of the sender, the message content, id of the message it was replied to, and if the message was pinned.    
                        data[str(x.id)] = [x.id, int(x.date.timestamp()), x.from_id.user_id, x.text, replied, x.pinned]
            except:
                print(x.text)

        reply_number = data[msg_id][4]
        my_dict = []
        write_history = ''
        try:
            #Checking for past replies given msg id
            while reply_number is not None:
                my_dict.append([reply_number, data[str(reply_number)][2]])
                reply_number = data[str(reply_number)][4]
                #Storing max 3 past messages
                if len(my_dict) > max_memory_message + 1:
                    break
        except Exception as e:
            print(e)
            
        #Checking for history    
        if len(my_dict) > 1:
            #Building message history/memory
            for i in range(len(my_dict) - 1, -1, -1):
                if str(my_dict[i][1]) == my_bot_id:
                    #If message comes from bot -> message is treated as response from person A
                    write_history += "A: " + data[str(my_dict[i][0])][3] + "\n"
                else:
                    #Else-> message is treated as response from telegram user
                    write_history += "Q: " + data[str(my_dict[i][0])][3] + "\n"

        
        return write_history

