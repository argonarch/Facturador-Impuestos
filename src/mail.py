from imap_tools.mailbox import MailBox
from imap_tools.query import A
import datetime
import re
import messenger
import os
from dotenv import load_dotenv

load_dotenv()
now = datetime.datetime.now()
print(now)
fecha = datetime.date(now.year, now.month - 1, 1)

host = os.environ["HOST"]
password = os.environ["PASSWORD"]
username = os.environ["USERNAME"]
mail_edesur = os.environ["MAIL_EDESUR"]
mail_aysa = os.environ["MAIL_AYSA"]
mail_metrogas = os.environ["MAIL_METROGAS"]
asunto_edesur = os.environ["ASUNTO_EDESUR"]
asunto_aysa = os.environ["ASUNTO_AYSA"]
asunto_metrogas = os.environ["ASUNTO_METROGAS"]


def buscador():
    print("Iniciando")
    with MailBox(host).login(username, password) as mailbox:
        print("Edesur")
        for msg in mailbox.fetch(
            A(from_=mail_edesur, subject=asunto_edesur, date_gte=fecha)
        ):
            filter(
                "Edesur",
                msg.html,
                msg.date,
                r"[0-9]{2}/[0-9]{2}/[0-9]{4}",
                r"\$<strong>([0-9]{1,}\.[0-9]{2})",
            )
        print("Metrogas")
        for msg in mailbox.fetch(
            A(from_=mail_metrogas, subject=asunto_metrogas, date_gte=fecha)
        ):
            filter(
                "Metrogas",
                msg.html,
                msg.date,
                r": ([0-9]{2}\.[0-9]{2}\.[0-9]{4})",
                r"\$.([0-9]{1,}\.[0-9]{1,}\,[0-9]{2})",
            )
        print("Aysa")
        for msg in mailbox.fetch(
            A(from_=mail_aysa, subject=asunto_aysa, date_gte=fecha)
        ):
            filter(
                "Aysa",
                msg.html,
                msg.date,
                r"[0-9]{2}/[0-9]{2}/[0-9]{4}",
                r"\$.([0-9]{1,}\.[0-9]{1,}\,[0-9]{2})",
            )


def filter(name, htmlText, dateText, redoxFv, redoxPv):
    f = datetime.date(dateText.year, dateText.month, dateText.day)
    fv = strList(re.findall(redoxFv, htmlText))
    pv = strList(re.findall(redoxPv, htmlText))
    print("Servicio", name, "Fecha:", f, "Vencimiento:", fv, "Precio: $", pv)
    messenger.sendMessages(name, pv, fv, f)


# Function to convert
def strList(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


buscador()
