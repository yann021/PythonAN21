value = input("saisir un nombre \n ->")
value = int(value)
i = 1
result = 0

while(i<20):
    result = value*i
    if (result % 3 == 0):
        print("*",result, "*")
        print("coucou")
    else:
       print(result) 
    i+=1