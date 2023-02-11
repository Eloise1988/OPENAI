# Telegram Chatbot with Memory using OpenAI
![AskGpt](https://github.com/Eloise1988/OPENAI/blob/main/PNG/askgpt.jpeg)
This is an asyncronous function that serves as a Telegram bot using OpenAI's GPT-3 language model.
This is a python script for a Telegram chatbot that uses the OpenAI API to generate responses to user input.

## [Medium Publication](https://levelup.gitconnected.com/create-your-own-hilarious-chatgpt-bot-in-telegram-with-python-a-step-by-step-guide-466e8a510c0d) + [Testing](https://t.me/askchatgpt) 

## Requirements
* A Telegram bot API key, obtained by creating a bot on Telegram.
* An OpenAI API key, obtained by creating an account on OpenAI.
* Python 3 and the following libraries: requests, json, os, threading, asyncio and memory (in the current folder: gets last messages in the group)

## How to use
1. Clone the repository and navigate to the directory.
2. A. Fill in the following in the `robotV2.py` script with your own API keys and desired settings. 
- `BOT_TOKEN`: The token you get from Telegram when you create your bot.
- `ALLOWED_GROUP_ID` : the list of allowed group_ids
- `API_KEY` : OpenAI secret Key
- `CHATBOT_HANDLE` : Bot name
- `BOT_ID` : Bot name

B. Fill in the following in the `memory.py` script with your own settings and authentication. 
- `api_id`: Telegram API ID and Hash (you can get it from my.telegram.org)
- `api_hash` : Telegram API Hash (you can get it from my.telegram.org)
- `session_hash` : Telegram Session Hash 
```
  async with TelegramClient('session_file', api_id, api_hash) as client:
      # Connect to the Telegram servers and log in
      await client.start()

      # After logging in, the session hash will be automatically generated and stored
      # in the 'session_file' file, which you can use in future runs to log in with
      # the same session:
      session_hash = client.session.save()

      print(str(session_hash))
```
- `my_bot_id` : Bot ID number
- `max_memory_message` : Stored number of max messages

3. Run the script with the command `python robotV2.py`
4. Add the bot to a Telegram group, and mention the bot's username in a message to generate a response from the OpenAI API.

## Functionality

1. This bot limits access to only a group of initially specified groups in variable `ALLOWED_GROUP_ID`
2. This bot has a list of pre-defined tones (e.g. friendly, professional, humorous) stored in the `tone_list` variable that it can respond in.
3. This function checks for new messages in a Telegram group by sending a GET request to the Telegram API and parsing the response data using the `requests` and `json` modules.
4. This bot sends greeting messages to new participants
5. This bot can also respond to commands such as '/img' for generating image captions and the bot's username for answering questions.
6. This bot also has an option to include the user's historical message to the context of the chatbot response using the `write_history` variable.

## Variables

- `filename`: a string variable that stores the filepath and name of the text file where the last ID message is stored.
- `bot_personality`: a string variable that stores the personality of the bot.
- `write_history`: a string variable that stores the historical message of the user.
- `tone_list`: a list variable that stores the pre-defined tones for the bot to respond in.
- `last_update`: a variable that stores the last ID message from the text file.
- `url`: a variable that stores the URL for the Telegram API to retrieve updates.
- `response`: the response data from the Telegram API.
- `data`: the parsed JSON data from the Telegram API response.
- `result`: the last message in the Telegram group.
- `msg_id`: the id of the message received
- `boolean_active`: a boolean flag to check if the bot is active
- `prompt1`: The prompt after checking the tone
- `prompt`: the user's message

## Functions

- `openAI` : function to call the OpenAI API to generate the text response.
- `openAImage` : function to call the OpenAI API to generate image caption.
- `telegram_bot_sendtext` : function to send the text response to the user through Telegram API.
- `telegram_bot_sendimage` : function to send the image caption to the user through Telegram API.
- `checkTone` : function to check the tone of the question and set the bot_personality accordingly.
- `memory.get_channel_messages` : function to retrieve the user's historical messages from the Telegram group.
