# -*- coding: utf-8 -*-
import time
import requests

tg_token = "token here"
channel = "@example"

while True :
    def postnekopic():
        picURL = requests.get(f"https://nekos.life/api/v2/img/neko").json()['url']
        r = requests.get("https://api.telegram.org/bot"+tg_token+"/sendPhoto?chat_id="+channel+"&photo="+picURL+"&caption=%23neko" )
    def postbakapic():
        picURL = requests.get(f"https://nekos.life/api/v2/img/baka").json()['url']
        r = requests.get("https://api.telegram.org/bot"+tg_token+"/sendPhoto?chat_id="+channel+"&photo=" + picURL + "&caption=%23baka")
    def postfoxgirlpic():
        picURL = requests.get(f"https://nekos.life/api/v2/img/fox_girl").json()['url']
        r = requests.get("https://api.telegram.org/bot"+tg_token+"/sendPhoto?chat_id="+channel+"&photo=" + picURL + "&caption=%23fox_girl")
    def postpokepic():
        picURL = requests.get(f"https://nekos.life/api/v2/img/poke").json()['url']
        r = requests.get("https://api.telegram.org/bot"+tg_token+"/sendPhoto?chat_id="+channel+"&photo=" + picURL + "&caption=%23poke")
    def postkisspic():
        picURL = requests.get(f"https://nekos.life/api/v2/img/kiss").json()['url']
        r = requests.get("https://api.telegram.org/bot"+tg_token+"/sendPhoto?chat_id="+channel+"&photo=" + picURL + "&caption=%23kiss")

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
