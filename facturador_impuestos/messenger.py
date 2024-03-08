import requests

def get_url(msg):
    my_token = '6049411213:AAFzNRdrgejNj0HMqjJ_t5t593ZDySSw7LI'
    chat_id = '-1001477006866'
    return f"https://api.telegram.org/bot{my_token}/sendMessage?chat_id={chat_id}&text={msg}"

def sendMessages(tittle, price, expiration, timeCheck):
    msgTittle = f'Nueva factura {tittle} emitida el {timeCheck}'
    requests.get(get_url(msgTittle)).json() 
    msgBody = f'El precio de la factura de {tittle} es de: {price} y su vencimiento es el {expiration}'
    requests.get(get_url(msgBody)).json() 
