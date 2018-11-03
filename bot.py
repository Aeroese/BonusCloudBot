#coding=utf-8
import time
import telebot
import datetime
import threading
import configparser
import urllib3
import requests

from APITools import *
from telebot import types
from APISubscribe import *
from base.APIMessage import *
from APISender import APISender
from BonusCloud import BonusCloud

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.adapters.DEFAULT_RETRIES = 3

config = configparser.ConfigParser()
config.read('Config.ini')
Email = config.get('BonusCloud','Email')
Password = config.get('BonusCloud','Password')
Chatid= int(config.get('BonusCloud','Chatid'))
bot = telebot.TeleBot(config.get('BonusCloud','Token'))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hello , I am BonusCloudBot , you can receive your bonuscloud income at 6:30 every morning !')

@bot.message_handler(commands=['get'])
def send_get(message):
    code = BonusCloud.Login(Email,Password)['code']
    if code == 200 :
        bot.send_message(reply_to_message_id = message.message_id, chat_id = message.chat.id, text = 'Login success , get income ...')
        try:
            year = str(datetime.datetime.now().year) + '-'
            month = str(datetime.datetime.now().month) + '-'
            day = str(datetime.datetime.now().day)
            text = year + month + day + '\nToday : ' + str(BonusCloud.GetTodayRevenue()['ret']['revenue']) + '\nRefer : ' + str(BonusCloud.GetReferRevenue()['ret']['revenue']) + '\nTotal : ' +   str(BonusCloud.GetTotalRevenue()['ret']['revenue'])
        except:
            text = 'No get income !'
        bot.send_message(reply_to_message_id = message.message_id, chat_id = message.chat.id, text = text)
    else :
        bot.send_message(reply_to_message_id = message.message_id, chat_id = message.chat.id, text = 'No login !')

@bot.message_handler(commands = ['test'])
def send_test(message):
    bot.send_message(reply_to_message_id = message.message_id, chat_id = message.chat.id, text = 'it is a test message')

def task() :
    print('BonusCloudBot started.')
    while True:
        for t2 in config.get('BonusCloud','time').split(',') :
            time2 = t2.split(':')
            now = datetime.datetime.now()
            if now.hour == int(time2[0]) and now.minute == int(time2[1]):
                t = threading.Thread(target = getincome)
                t.start()
                time.sleep(60)
        time.sleep(10)
def getincome() :
    code = BonusCloud.Login(Email,Password)['code']
    if code == 200 :
        try:
            year = str(datetime.datetime.now().year) + '-'
            month = str(datetime.datetime.now().month) + '-'
            day = str(datetime.datetime.now().day)
            message = year + month + day + '\nToday : ' + str(BonusCloud.GetTodayRevenue()['ret']['revenue']) + '\nRefer : ' + str(BonusCloud.GetReferRevenue()['ret']['revenue']) + '\nTotal : ' +   str(BonusCloud.GetTotalRevenue()['ret']['revenue'])
        except:
            message = 'No get income !'
        bot.send_message(chat_id = Chatid, text = message)
    else :
        bot.send_message(chat_id = Chatid, text = 'No login !')
if __name__ == '__main__':
    # pip install pyTelegramBotAPI
    timer = threading.Timer(1, task)
    timer.start()
    while True:
        try:
            bot.polling(none_stop=True)
            time.sleep(30)
        except:
            print("403")
