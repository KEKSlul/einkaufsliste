einkaufsliste = []
einkaufsliste.append(input("Was möchtest du noch einkaufen:"))
print (einkaufsliste)
Sache = ""
while Sache != "fertig": 
    input("Noch etwas? Ansonsten schreib fertig")
    einkaufsliste.append(Sache)
    if Sache != "fertig":
        print("Zeit zum einkaufen! Hier nochmal die List")
