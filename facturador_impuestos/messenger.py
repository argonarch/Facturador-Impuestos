import requests

new_line = '\n'

def get_url(msg):
    my_token = '6049411213:AAFzNRdrgejNj0HMqjJ_t5t593ZDySSw7LI'
    chat_id = '-1001477006866'
    return f"https://api.telegram.org/bot{my_token}/sendMessage?chat_id={chat_id}&text={msg}"

def sendMessages(tittle, price, expiration, timeCheck):
    msgBody = f'Factura {tittle} {new_line} Emision: {timeCheck} {new_line} Precio: {price} {new_line} Vencimiento: {expiration}'
    requests.get(get_url(msgBody)).json() 
