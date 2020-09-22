a = "Ma jeunesse ne fut qu'un ténébreux orage,\
    Traverse ca et la par de brillants soleils\
    Le tonnerre est la pluie ont fait un tel ravage\
    qu il reste en mon jardin bien peu de fruits de vermeils"

Stat = {}

for x in a:
    lettre = x.lower()
    if(Stat.get(x)):
        Stat[x] +=1
    else:
        Stat[x] = 1
    
print(Stat)

maimounab537@gmail.com