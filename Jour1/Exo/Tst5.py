#Créer un imput
Value = input("Saisir une valeur \n -> ")
Value = int(Value)

#Créer un variable diviseur
Diviseur = 2
nb_premier = True

# Boucle 
while (Diviseur<Value):
    if (Value%Diviseur == 0):
        nb_premier = False
        print(Diviseur, 'est un diviseur de', Value)
    Diviseur +=1
    

#afficher le resultat
if (nb_premier == True):
    print(Value, 'est un nombre nb_premier')
