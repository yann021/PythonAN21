table=int(input("Quelle table voulez vous afficher? "))
liste=[]
for i in range(1,21):
    res=i*table
    if res%3==0:
        liste.append(str(res)+'*')
    else:
        liste.append(res)

print(liste)