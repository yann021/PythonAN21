n=int(input("Entrer un nombre: "))
diviseur=2
is_prime=True
while diviseur<n:
    if n%diviseur==0:
        is_prime=False
        print(diviseur, "est un diviseur de ",n)
    diviseur+=1

if is_prime:
    print(n, "est un nombre premier")