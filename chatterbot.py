from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/'):
    for file in os.listdir('chatterbot-corpus-master/chatterbot_corpus/data/'+files):
        data=open('chatterbot-corpus-master/chatterbot_corpus/data/'+files+"/"+file,'r',encoding="utf8").readlines()
        bot.train(data)
while True:
    message=input('You:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('Chatbot:',reply)
    if message.strip()=='Bye' or message.strip()=='bye':
        print('Chatbot:Bye')
        break