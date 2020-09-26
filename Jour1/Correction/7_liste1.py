ma_liste=[]
while True:
    n=input('Entrer un nombre: ')
    if n=='q':
        break
    else:
        if int(n) not in ma_liste:
            ma_liste.append(int(n))

print(ma_liste.sort())

print("Max: ",max(ma_liste))
print("Min: ",min(ma_liste))