import os
import time

import requests
import colorama
from dotenv import load_dotenv
import datetime

load_dotenv()

colorama.init(autoreset=True)

# takes the token and channel tag from the .env file
TOKEN = os.environ.get("TOKEN")
CHANNEL = os.environ.get("CHANNEL")


# takes the url of an image and sends it to the Telegram channel and handles connection exceptions
def post_neko_pic(TOKEN, CHANNEL):
    try:
        url_neko_pic = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHANNEL}&photo={url_neko_pic}&caption=%23neko"
        )
        posting_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"Neko picture posted at: {posting_time}\n"
        )
    except requests.ConnectionError:
        error_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.RED
            + "[X] "
            + colorama.Fore.WHITE
            + f"A connection error occurred at {error_time}. Check you internet! ;)\n"
        )
        pass


def post_baka_pic(TOKEN, CHANNEL):
    try:
        url_baka_pic = requests.get("https://nekos.life/api/v2/img/baka").json()["url"]
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHANNEL}&photo={url_baka_pic}&caption=%23baka"
        )
        posting_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"Foxgirl picture posted at: {posting_time}\n"
        )
    except requests.ConnectionError:
        error_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.RED
            + "[X] "
            + colorama.Fore.WHITE
            + f"A connection error occurred at {error_time}. Check you internet! ;)\n"
        )
        pass


def post_foxgirl_pic(TOKEN, CHANNEL):
    try:
        url_foxgirl_pic = requests.get("https://nekos.life/api/v2/img/fox_girl").json()[
            "url"
        ]
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHANNEL}&photo={url_foxgirl_pic}&caption=%23fox_girl"
        )
        posting_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"Poke picture posted at: {posting_time}\n"
        )
    except requests.ConnectionError:
        error_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.RED
            + "[X] "
            + colorama.Fore.WHITE
            + f"A connection error occurred at {error_time}. Check you internet! ;)\n"
        )
        pass


def post_poke_pic(TOKEN, CHANNEL):
    try:
        url_poke_pic = requests.get("https://nekos.life/api/v2/img/poke").json()["url"]
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHANNEL}&photo={url_poke_pic}&caption=%23poke"
        )
        posting_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"Baka picture posted at: {posting_time}\n"
        )
    except requests.ConnectionError:
        error_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.RED
            + "[X] "
            + colorama.Fore.WHITE
            + f"A connection error occurred at {error_time}. Check you internet! ;)\n"
        )
        pass


def post_kiss_pic(TOKEN, CHANNEL):
    try:
        url_kiss_pic = requests.get("https://nekos.life/api/v2/img/kiss").json()["url"]
        r = requests.get(
            f"https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHANNEL}&photo={url_kiss_pic}&caption=%23kiss"
        )
        posting_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.GREEN
            + "[V] "
            + colorama.Fore.WHITE
            + f"Kiss picture posted at: {posting_time}\n"
        )
    except requests.ConnectionError:
        error_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(
            colorama.Fore.RED
            + "[X] "
            + colorama.Fore.WHITE
            + f"A connection error occurred at {error_time}. Check you internet! ;)\n"
        )
        pass


# Sends a different image every 60 minutes (3600 seconds)
while True:
    post_neko_pic(TOKEN, CHANNEL)
    time.sleep(3600)

    post_foxgirl_pic(TOKEN, CHANNEL)
    time.sleep(3600)

    post_poke_pic(TOKEN, CHANNEL)
    time.sleep(3600)

    post_baka_pic(TOKEN, CHANNEL)
    time.sleep(3600)

    post_kiss_pic(TOKEN, CHANNEL)
    time.sleep(3600)
