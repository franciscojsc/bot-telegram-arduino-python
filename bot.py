# -*- coding: utf-8 -*-
import telepot
import os
from pyfirmata import Arduino, util
  
def handleCommad(content) :
  try:
    chat_id = content['chat']['id']
    command = content['text']

    if command == 'Hi' :
      mensage = 'Hello, how are you?'
      bot.sendMessage(chat_id, mensage)

    if command == '/on' :
      setDigitalPinState(my_board, 13, 1)
      sendMessage(chat_id, 'Led turn on')

    if command == '/off' :
      setDigitalPinState(my_board, 13, 0)
      sendMessage(chat_id,'Led turn off')

  except :
     bot.sendMessage(chat_id, 'There was an error!!!')

def configBoard(port) :
  return Arduino(port)

def setDigitalPinState(board, pin, state) :
  board.digital[pin].write(state)

def sendMessage(chat, mensage) :
  bot.sendMessage(chat, mensage)

token_telegram = os.environ["TELEGRAM_TOKEN"]
my_board = configBoard('/dev/ttyACM0')
bot = telepot.Bot(token_telegram)
bot.message_loop(handleCommad)

try:
  print('press CTRL + C to cancel')

  while True :
    pass
    
except KeyboardInterrupt :
  print('Bye')
