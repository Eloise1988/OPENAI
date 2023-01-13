# Telegram Chatbot using OpenAI
![AskGpt](https://github.com/Eloise1988/OPENAI/blob/main/PNG/askgpt.jpeg)
This is a python script for a Telegram chatbot that uses the OpenAI API to generate responses to user input.

## [Medium Publication](https://levelup.gitconnected.com/create-your-own-hilarious-chatgpt-bot-in-telegram-with-python-a-step-by-step-guide-466e8a510c0d) 

## Requirements
* A Telegram bot API key, obtained by creating a bot on Telegram.
* An OpenAI API key, obtained by creating an account on OpenAI.
* Python 3 and the following libraries: requests, json, os, threading

## How to use
1. Clone the repository and navigate to the directory.
2. Fill in the API_KEY, MODEL, BOT_TOKEN and BOT_PERSONALITY in the script with your own API keys and desired settings.
3. Run the script with the command python chatbot.py
4. Add the bot to a Telegram group, and mention the bot's username in a message to generate a response from the OpenAI API.

## Functionality
### Imports and setup
1. The script starts by importing the necessary libraries and setting up the API clients.
### openAI function
2. The openAI() function is defined, which takes a user input (prompt) and sends a request to the OpenAI API to generate a response. The function then returns the response.
### telegram_bot_sendtext function
3. The telegram_bot_sendtext() function is defined, which takes a message, a chat ID, and a message ID, and sends the message as a response to the Telegram group using the Telegram Bot API.
### Chatbot function
4. The Chatbot() function is defined which retrieves the latest requests from users in a Telegram group, generates a response using the OpenAI API, and sends the response back to the group. The function retrieves the last ID message from the text file for the ChatGPT update, check for new messages in Telegram group, check that user mentionned chatbot's username in message, calling OpenAI API using the bot's personality and sending back response to telegram group.

## Global Variables
The script also uses a few global variables such as the API key for OpenAI, the model to use with the OpenAI API, the Telegram bot API key, and the bot's personality as defined by a set of adjectives.

## Note
This script is provided as a starting point, and can be further customized and expanded upon as needed.

## License
This project is licensed under the MIT License.



