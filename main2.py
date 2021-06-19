# -*- coding: utf-8 -*-
import time
import requests

tg_token = "token"
channel = "@example"

def response(r):
    if r['ok'] is True:
        print('[' + time.ctime(time.time()) + ']', 'OK:', r['ok'], ';#' + str(r['result']['message_id']))
    else:
        print('[' + time.ctime(time.time()) + ']', 'OK:', r['ok'], '; Error:',r['error_code'],'\n',r['description'],)

while True:
    def postnekopic():
        picURL = requests.get("https://nekos.life/api/v2/img/neko").json()['url']
        r = requests.get(
            "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23neko").json()
        response(r)

    def postbakapic():
        picURL = requests.get("https://nekos.life/api/v2/img/baka").json()['url']
        r = requests.get(
            "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23baka").json()
        response(r)

    def postfoxgirlpic():
        picURL = requests.get("https://nekos.life/api/v2/img/fox_girl").json()['url']
        r = requests.get(
            "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23fox_girl").json()
        response(r)

    def postpokepic():
        picURL = requests.get("https://nekos.life/api/v2/img/poke").json()['url']
        r = requests.get(
            "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23poke").json()
        response(r)

    def postkisspic():
        picURL = requests.get("https://nekos.life/api/v2/img/kiss").json()['url']
        r = requests.get(
            "https://api.telegram.org/bot" + tg_token + "/sendPhoto?chat_id=" + channel + "&photo=" + picURL + "&caption=%23kiss").json()
        response(r)

    postnekopic()
    time.sleep(3600)
    postfoxgirlpic()
    time.sleep(3600)
    postpokepic()
    time.sleep(3600)
    postbakapic()
    time.sleep(3600)
    postnekopic()
    time.sleep(100)
    postkisspic()
    time.sleep(3600)
