import requests
import os
from dotenv import load_dotenv

load_dotenv()
new_line = "\n"

my_token = os.environ["MY_TOKEN"]
chat_id = os.environ["CHAT_ID"]


def get_url(msg):
    return f"https://api.telegram.org/bot{my_token}/sendMessage?chat_id={chat_id}&text={msg}"


def sendMessages(tittle, price, expiration, timeCheck):
    msgBody = f"Factura {tittle} {new_line} Emision: {timeCheck} {new_line} Precio: {price} {new_line} Vencimiento: {expiration}"
    requests.get(get_url(msgBody)).json()
