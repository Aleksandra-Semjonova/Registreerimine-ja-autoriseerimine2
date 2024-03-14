def loe_failist(fail:str)->list:
    """ Loeme failist read ja salvestame j�rjendisse. Funktsioon tagastab �rjend
    :param str fail: 
    :rtype: list
    """
    f=open(fail,'r',encoding="utf-8") #try
    j�rjend=[]
    for rida in f:
        j�rjend.append(rida.strip())
    f.close()
    return j�rjend


def kirjuta_failisse(fail:str,j�rjend=[]):
    """ Funktsion �mber kirjutab andmed failisse
    :param str fail:
    :param list j�rjend:
    """
    n=int(input("Sisesta mitu elementi: "))
    for i in range (n):
        j�rjend.append(input("{}. elemend ".format(i+1)))
    f=open(fail,'w',encoding="utf-8")
    for el in j�rjend:
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

p�evad=loe_failist("p�evad.txt")
print(p�evad)
