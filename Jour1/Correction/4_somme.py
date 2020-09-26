n=int(input("Entrez un nombre: "))

#avec for
total=0
for i in range(n+1):
    total+=i

#Avec while
total=0
while(n>0):
    total+=n
    n-=1
print(total)