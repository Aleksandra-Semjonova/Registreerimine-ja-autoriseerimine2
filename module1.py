import random

def registreerimine(k:list,p:list)->any:

    """ 
    Funktsioon loob uue kasutaja
    :param list k: kasutajas järjend
    :param list p: parool järjend
    :rtype: any
    """
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi=="":
            print("Kasutajanimel peab olema nimi.")
            print("")
        elif nimi in k:
            print("See nimi on hõivatud, proovige teist.")
            print("")
        else:
            break
    
    while True:
        parool=input("Sisesta parool: ")
        str0=".,:;!_*-+()/#¤%&"
        str1='0123456789'
        str2='qwertyuiopasdfghjklzxcvbnm'
        str3=str2.upper()
        str4=str0 + str1 + str2 + str3
        ls=list(str4)
        random.shuffle(ls)
        parool=''.join([random.choice(ls) for x in range(12)])
       
        if parool=="":
            print("Parool ei saa olla tühi.")
            print("")
        else:
            break
def autoriseerimine(k: list, p: list) -> bool:
    """
    Autoriseerib kasutaja süsteemi tagasi.

    :param list k: kasutajas järjend
    :param list p: parool järjend
    :rtype: bool
    """
    while True:
        kasutajas=input("Sisesta kasutajanimi: ")
        parool=input("Sisesta parool: ")
        if kasutajas in k and parool==p[k.index(kasutajas)]:
            print("Olete sisse logitud.")
            print("")
            return True
        else:
            print("Vigane kasutajanimi või parool,proovi uuesti.")
            print("")

def muuda_parool(k:list,p:list)->any:
    """
    Muudab kasutaja parooli.

    :param list k: kasutajas järjend
    :param list p: Parool järjend
    :rtype: any
    """
    while True:
        kasutajas=input("Sisesta oma kasutajanimi: ")
        if kasutajas not in k:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index=k.index(kasutajas)
            break

    while True:
        muutmine=input("Mida soovite oma nime või parooli muuta?: ")
        if muutmine=="nime":
            uus_kasutaja=input("Sisesta uus nimi: ")
            if  uus_kasutaja in k:
                print("See nimi on juba kasutusel.")
                print("")
                continue
            else:
                k[index]=uus_kasutaja
                print("Nimi edukalt muudetud.")
                print("")
                break
        elif muutmine=="parool":
            parool_uus=input("Sisesta uus parool: ")
            if parool_uus=="":
                print("Parool ei saa olla tühi.")
                print("")
                continue
            else:
                p[index]=parool_uus
                print("Parool edukalt muudetud.")
                print("")
                break
        else:
            print("Vigane valik. Palun vali 'N' või 'P'.")
            print("")  


       
#def send_to_email()
import smtplib
import ssl
from email.message import EmailMessage
def unustatud_parool(k: list, p: list) -> None:
    """
    Saadab unustatud parooli e-kirja kasutajale.

    :param list k: kasutajas järjend
    :param list p: Parool järjend
    """
    while True:
        nimi = input("Sisesta oma kasutajanimi: ")
        if nimi not in k:
            print("Sellist kasutajanime ei ole.")
            print("")
            continue
        else:
            index = k.index(nimi)
            break

    email = input("Sisesta oma e-posti aadress: ")
    if email == "":
        print("E-posti aadress ei saa olla tühi.")
        return

    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "Aleksandra.semjonova24@gmail.com"
    password = input("Sisestage oma e-posti parool: ")
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(f"Teie parool on: {p[index]}")
    msg['Subject'] = "Unustatud parool"
    msg['From'] = "Aleksandra.semjonova24@gmail.com"
    msg['To'] = email

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.send_message(msg)
    except:
       print("Viga")