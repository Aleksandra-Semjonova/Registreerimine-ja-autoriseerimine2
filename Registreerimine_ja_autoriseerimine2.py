from module1 import * 

kasutaja=[]
paroolid=[]
while True:
    operatsioon=print("Registreerimine-1\nAutoriseerimine-2\nNime või parooli muutmine-3\nUnustanud parooli taastamine-4\nLõpetamine-5")
    vastus=str(input()).capitalize()
    if vastus=="1":
        kasutaja, paroolid=registreerimine(kasutaja,paroolid)
        print(kasutaja,paroolid)
        print("")
    elif vastus=="2":
        autoriseerimine(kasutaja,paroolid)
    elif vastus=="3":
        muuda_parool(kasutaja,paroolid)
        print(kasutaja,paroolid)
    elif vastus=="4":
        unustatud_parool(kasutaja,paroolid)
    elif vastus=="5":
        break
    else:
        print("Palun vali toiming siit nimekirjast")