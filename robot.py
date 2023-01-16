# 1. Start by importing the necessary libraries and setting up the API clients 
import requests
import json
import os
import threading

# OpenAI secret Key
API_KEY = 'xxxxxxxxxxxsecretAPIxxxxxxxxxx'
# Models: text-davinci-003,text-curie-001,text-babbage-001,text-ada-001
MODEL = 'text-davinci-003'
# Telegram secret access bot token
BOT_TOKEN = 'xxxxxxbotapikeyxxxxx'
# Defining the bot's personality using adjectives
BOT_PERSONALITY = 'Answer in a funny tone, '

# 2a. Function that gets the response from OpenAI's chatbot
def openAI(prompt):
    # Make the request to the OpenAI API
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'model': MODEL, 'prompt': prompt, 'temperature': 0.4, 'max_tokens': 300}
    )

    result = response.json()
    final_result = ''.join(choice['text'] for choice in result['choices'])
    return final_result

# 2b. Function that gets an Image from OpenAI
def openAImage(prompt):
    # Make the request to the OpenAI API
    resp = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={'Authorization': f'Bearer {API_KEY}'},
        json={'prompt': prompt,'n' : 1, 'size': '1024x1024'}
    )
    response_text = json.loads(resp.text)
      
    return response_text['data'][0]['url']
  
# 3a. Function that sends a message to a specific telegram group
def telegram_bot_sendtext(bot_message,chat_id,msg_id):
    data = {
        'chat_id': chat_id,
        'text': bot_message,
        'reply_to_message_id': msg_id
    }
    response = requests.post(
        'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage',
        json=data
    )
    return response.json()

# 3b. Function that sends an image to a specific telegram group
def telegram_bot_sendimage(image_url, group_id, msg_id):
    data = {
        'chat_id': group_id, 
        'photo': image_url,
        'reply_to_message_id': msg_id
    }
    url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto'
    
    response = requests.post(url, data=data)
    return response.json()
  
# 4. Function that retrieves the latest requests from users in a Telegram group, 
# generates a response using OpenAI, and sends the response back to the group.
def Chatbot():
    # Retrieve last ID message from text file for ChatGPT update
    cwd = os.getcwd()
    filename = cwd + '/chatgpt.txt'
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("1")
    else:
        print("File Exists")    

    with open(filename) as f:
        last_update = f.read()
        
    # Check for new messages in Telegram group
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update}'
    response = requests.get(url)
    data = json.loads(response.content)
        
    for result in data['result']:
        try:
            # Checking for new message
            if float(result['update_id']) > float(last_update):
                # Checking for new messages that did not come from chatGPT
                if not result['message']['from']['is_bot']:
                    last_update = str(int(result['update_id']))
                    
                    # Retrieving message ID of the sender of the request
                    msg_id = str(int(result['message']['message_id']))
                    
                    # Retrieving the chat ID 
                    chat_id = str(result['message']['chat']['id'])
                    
                    # Checking if user wants an image
                    if '/img' in result['message']['text']:
                        prompt = result['message']['text'].replace("/img", "")
                        bot_response = openAImage(prompt)
                        print(telegram_bot_sendimage(bot_response, chat_id, msg_id))
                    # Checking that user mentionned chatbot's username in message
                    if '@ask_chatgptbot' in result['message']['text']:
                        prompt = result['message']['text'].replace("@ask_chatgptbot", "")
                        # Calling OpenAI API using the bot's personality
                        bot_response = openAI(f"{BOT_PERSONALITY}{prompt}")
                        # Sending back response to telegram group
                        print(telegram_bot_sendtext(bot_response, chat_id, msg_id))
                    # Verifying that the user is responding to the ChatGPT bot
                    if 'reply_to_message' in result['message']:
                        if result['message']['reply_to_message']['from']['is_bot']:
                            prompt = result['message']['text']
                            bot_response = openAI(f"{BOT_PERSONALITY}{prompt}")
                            print(telegram_bot_sendtext(bot_response, chat_id, msg_id))
        except Exception as e: 
            print(e)

    # Updating file with last update ID
    with open(filename, 'w') as f:
        f.write(last_update)
    
    return "done"

# 5 Running a check every 5 seconds to check for new messages
def main():
    timertime=5
    Chatbot()   
    # 5 sec timer
    threading.Timer(timertime, main).start()

# Run the main function
if __name__ == "__main__":
    main()
