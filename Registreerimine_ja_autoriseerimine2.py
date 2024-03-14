from module1 import * 

kasutaja=[]
paroolid=[]
while True:
    operatsioon=print("Registreerimine(R)\nAutoriseerimine(A)\nNime või parooli muutmine(M)\nUnustanud parooli taastamine(U)\nLõpetamine(L)")
    vastus=str(input()).capitalize()
    if vastus=="R":
        registreerimine(kasutaja,paroolid)
        print(kasutaja,paroolid)
        print("")
    elif vastus=="A":
        autoriseerimine(kasutaja,paroolid)
    elif vastus=="M":
        muuda_parool(kasutaja,paroolid)
        print(kasutaja,paroolid)
    elif vastus=="U":
        unustatud_parool(kasutaja,paroolid)
    elif vastus=="L":
        break
    else:
        print("Palun vali toiming siit nimekirjast")