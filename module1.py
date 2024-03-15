import random

def kirjuta_failisse(fail:str, järjend=[], järjend2=[]):
    """ Funktsion ümber kirjutab andmed failisse
    :param str fail: Faili nimi
    :param list järjend: esimene järjend
    :param list järjend2: teine järjend
    :rtype: any
    """
    existing_data = []
    try:
        with open(fail, 'r', encoding="utf-8") as v:
            for line in v:
                existing_data.append(line.strip())
    except FileNotFoundError:
        pass

    with open(fail, 'a', encoding="utf-8") as f:
        for i in range(len(järjend)):
            nimi = str(järjend[i])
            parool = str(järjend2[i])
            entry = nimi + ": " + parool + "\n"
            if not any(nimi in line for line in existing_data):
                f.write(entry)
    return järjend


def loe_pas_log(fail:str)-> any:

    log = []
    pas = []
    with open(fail, "r", encoding="utf-8") as f: 
        for line in f:
            n = line.find(":")
            log.append(line[0:n].strip())
            pas.append(line[n+1:].strip())
    return log, pas

def registreerimine(k:list,p:list)-> any:

    """ 
    Funktsioon loob uue kasutaja
    :param list k: kasutajas järjend
    :param list p: parool järjend
    :rtype: any
    """
    while True:
        result = loe_pas_log("Parool.txt")
        if result is None:
            log, pas = [], []
        else:
            log, pas = result
        nimi = input("Sisesta nimi: ")
        if nimi in log:
            print("See nimi on juba registreeritud.")
            print("")
        else:
            break 
    while True:
        valik = input("kas soovite parooli kirjutada(K) või selle genereerida?(G) ")
        if valik=="K":
            parool=input("Parool: ")
        elif valik=="G":
            str0 = ".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str0 + str1 + str2 + str3
            lt = list(str4)
            random.shuffle(lt)
            parool = ''.join([random.choice(lt) for x in range(12)])
        else:
            print("Palun vali 'sisesta' või 'gener'")
            print("")
            continue

def autoriseerimine(k: list, p: list) -> bool:
    """
    Autoriseerib kasutaja süsteemi tagasi.

    :param list k: kasutajas järjend
    :param list p: parool järjend
    :rtype: bool
    """
    while True:
        kasutajas=input("Kirjutage kasutajanimi: ")
        parool=input("Kirjutagparool: ")
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
        muuda=input("Mida soovite oma nime või parooli muuta?(nimi/parool): ")
        if muuda=="nimi":
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
        elif muuda=="parool":
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
            print("Vigane valik. Palun vali 'nimi' või 'parool'.")
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

    email= input("Sisesta oma e-posti aadress: ")
    if email== "":
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