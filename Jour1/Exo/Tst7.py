ma_list = []
Value = input("saisir une lettre \n ->")

while(Value!="q"):
    ma_list.append(Value)
    Value = input("saisir une lettre \n ->")

for nbr in ma_list:
    c=ma_list.count(nbr)
    if c>1:
        ma_list.remove(nbr)

print(ma_list)

#ma_list = []

#while (true)
#   n = input('Entrer une lettre')
#   if n == 'q':
#       break
#   else:
#       if n not in ma_list:
#           ma_list.append(n)
#print(ma_list)
#print(min(ma_list))