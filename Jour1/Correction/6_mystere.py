import random
mystere=random.randint(0,1000)
print(mystere)
essai=1
while (True):
    n=int(input("Entrez un nombre: "))
    if (n==mystere):
        break
    elif (n>mystere):
        print("Le nombre est plus petit")
    else:
        print("le nombre est plus grand")
    
    essai+=1

print("Vous avez mis",essai,"essais")