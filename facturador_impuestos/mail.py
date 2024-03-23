from imap_tools.mailbox import MailBox
from imap_tools.query import A
import datetime
import re
import messenger
import env

now = datetime.datetime.now()
print(now)
fecha = datetime.date(now.year, now.month - 1, 1)


def buscador():
    print("Iniciando")
    with MailBox(env.host).login(env.username, env.password) as mailbox:
        print("Edesur")
        for msg in mailbox.fetch(
            A(from_=env.mail_edesur, subject=env.asunto_edesur, date_gte=fecha)
        ):
            filter(
                "Edesur",
                msg.html,
                msg.date,
                "[0-9]{2}/[0-9]{2}/[0-9]{4}",
                "\$<strong>([0-9]{1,}\.[0-9]{2})",
            )
        print("Metrogas")
        for msg in mailbox.fetch(
            A(from_=env.mail_metrogas, subject=env.asunto_metrogas, date_gte=fecha)
        ):
            filter(
                "Metrogas",
                msg.html,
                msg.date,
                ": ([0-9]{2}\.[0-9]{2}\.[0-9]{4})",
                "\$.([0-9]{1,}\.[0-9]{1,}\,[0-9]{2})",
            )
        print("Aysa")
        for msg in mailbox.fetch(
            A(from_=env.mail_aysa, subject=env.asunto_aysa, date_gte=fecha)
        ):
            filter(
                "Aysa",
                msg.html,
                msg.date,
                "[0-9]{2}/[0-9]{2}/[0-9]{4}",
                "\$.([0-9]{1,}\.[0-9]{1,}\,[0-9]{2})",
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
