
Value = input("Saisir une valeur N \n -> ")
Value = int(Value)
#i = 0
Somme =0

#while i < Value:
#   i +=1
#   Somme += i
#print(Somme) 

for i in range(0, Value):
   Somme += i+1
   print(Somme)
print(Somme)