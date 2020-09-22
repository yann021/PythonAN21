
Value = input("Saisir une valeur N \n -> ")
Value = int(Value)
#i = 0
Somme =0

#while i < Value:
#   i +=1
#   Somme += i
#print(Somme) 

for i in range(Value+1):
   Somme += i
print(Somme)