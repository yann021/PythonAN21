a="Ma jeunesse ne fut qu'un tenebreux orage,\
   Traverse ca et la par de brillants soleils ;\
  Le tonnerre et la pluie ont fait un tel ravage,\
  Qu il reste en mon jardin bien peu de fruits vermeils."
mon_dict={}
for lettre in a:
    lettre=lettre.lower()
    if ord(lettre) >= ord('a') and ord(lettre)<ord('z'):
        mon_dict[lettre] = mon_dict.get(lettre,0)+1
        #Equivaut à:
        '''total=mon_dict.get(lettre,0)
        total+=1
        mon_dict[lettre]=total'''
print(mon_dict)