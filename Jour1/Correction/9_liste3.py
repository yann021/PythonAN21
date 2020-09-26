table=int(input("Quelle table voulez vous afficher? "))
liste=[]
for i in range(1,21):
    liste.append(i*table)

print(liste)