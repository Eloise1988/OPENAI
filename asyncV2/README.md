# Telegram Chatbot using OpenAI
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
2. Fill in the API_KEY, MODEL, BOT_TOKEN and ALLOWED_GROUP_ID in the script with your own API keys and desired settings.
3. Run the script with the command python robotV2.py
4. Add the bot to a Telegram group, and mention the bot's username in a message to generate a response from the OpenAI API.

## Functionality

1. Retrieves the last ID message from a text file for ChatGPT updates, and defines the filepath and name using the `filename` variable.
2. The bot has a list of pre-defined tones (e.g. friendly, professional, humorous) stored in the `tone_list` variable that it can respond in.
3. The function checks for new messages in a Telegram group by sending a GET request to the Telegram API and parsing the response data using the `requests` and `json` modules.
4. If there is a new message that did not come from the ChatGPT bot, it retrieves the chat ID of the sender and sends back a response to the Telegram group.
5. The bot can also respond to commands such as '/img' for generating image captions and the bot's username for answering questions.
6. The function also has an option to include the user's historical message to the context of the chatbot response using the `write_history` variable.
7. The `bot_personality` variable is used to store the personality of the bot.
8.  `openAI` and `openAImage` are used to call the OpenAI API to generate the text response or image caption.
9. `telegram_bot_sendtext` and `telegram_bot_sendimage` are used to send the response or image caption to the user through Telegram API.
10. `checkTone` is used to check the tone of the question and set the bot_personality accordingly.
11. `memory.get_channel_messages` is used to get the historical message of the user.

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
- `BOT_TOKEN`: The token you get from Telegram when you create your bot.
- `ALLOWED_GROUP_ID` : the list of allowed group_ids.
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
