import requests
import env
new_line = '\n'

def get_url(msg): 
    return f"https://api.telegram.org/bot{env.my_token}/sendMessage?chat_id={env.chat_id}&text={msg}"

def sendMessages(tittle, price, expiration, timeCheck):
    msgBody = f'Factura {tittle} {new_line} Emision: {timeCheck} {new_line} Precio: {price} {new_line} Vencimiento: {expiration}'
    requests.get(get_url(msgBody)).json() 
