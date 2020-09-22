import random
nombre_mystere=random.randint(0,100)
nombre_de_tour=1
Value = input("saisir un nombre \n ->")
Value = int(Value)

while (Value!=nombre_mystere):
    if (Value>nombre_mystere):
        print('Esseye encore, mais plus petit')
        Value = input("saisir un nombre \n ->")
        Value = int(Value)
        nombre_de_tour +=1
    elif (Value<nombre_mystere):
        print('Esseye encore, mais plus grand')
        Value = input("saisir un nombre \n ->")
        Value = int(Value)
        nombre_de_tour +=1
print('Enfin, il ta fallut', nombre_de_tour, 'fois')
