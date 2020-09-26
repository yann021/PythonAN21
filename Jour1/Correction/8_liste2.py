a = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
list_small=[]
list_long=[]
for element in a:
    if len(element)>=6:
        list_long.append(element)
    else:
        list_small.append(element)
    
print("La liste des petits prénoms est: ",list_small)
print("La liste des grands prénoms est: ",list_long)