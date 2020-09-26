liste=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
l1=[x for x in liste if len(x)>=6]
l2=[x for x in liste if len(x)<6]

a=  [x*20 if x%3!=0 else str(x)+'*' for x in range(1,21)]
 
print(l1,l2,a)