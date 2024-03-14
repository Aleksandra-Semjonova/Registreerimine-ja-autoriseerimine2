def loe_failist(fail:str)->list:
    """ Loeme failist read ja salvestame järjendisse. Funktsioon tagastab ärjend
    :param str fail: 
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8") #try
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend


def kirjuta_failisse(fail:str,järjend=[]):
    """ Funktsion ümber kirjutab andmed failisse
    :param str fail:
    :param list järjend:
    """
    n=int(input("Sisesta mitu elementi: "))
    for i in range (n):
        järjend.append(input("{}. elemend ".format(i+1)))
    f=open(fail,'w',encoding="utf-8")
    for el in järjend:
        f.write(el+"\n")
    f.close

from gtts import *
from os import system
def heli(tekst:str,keel:str):
    """
    :param tekst str:
    """
    obj=gtts(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisesta tekst: ")
heli(tekst,'et')

kirjuta_failisse("text.txt")

päevad=loe_failist("päevad.txt")
print(päevad)
