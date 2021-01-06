# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 18:34:44 2021

@author: nishant
"""
import logging
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)
logger= logging.getLogger(__name__)

TOKEN = your_token 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route(f'/{TOKEN}',methods= ['GET','POST'])
def webhook():
    
    update = Update.de_json(request.get_json(),bot)
    dp.process_update(update)
    return "OK"

def start(update, context):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi! {}".format(author)
    context.bot.send_message(update.effective_chat.id,reply)
    
def _help(update,context):
    help_txt = "Hey This is a help text!"
    context.bot.send_message(chat_id = update.effective_chat.id,text=help_txt)
    
def echo_text(update,context):
    
    reply= update.message.text
    context.bot.send_message(chat_id = update.effective_chat.id,text=reply)
    
def echo_sticker(update,context):
    
    context.bot.send_sticker(update.effective_chat.id, update.message.sticker.file_id)

def error(bot,update):
    
    logger.error("Update '%s' caused '%s'",update,update.error)



if __name__ == "__main__":
    
    bot =Bot(TOKEN)
    bot.set_webhook("https://example.io/"+TOKEN)
    
   
    dp=Dispatcher(bot,None)
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help',_help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    
    app.run(port=8443)

    
