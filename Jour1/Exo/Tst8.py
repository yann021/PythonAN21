ma_list = ['Jean','Maximilien','Brigitte','Sonia','Jean-Pierre','Sandra']
max6 = []
min6 = []

for i in ma_list:
    if (len(i)<6):
        min6.append(i)
    else:
        max6.append(i)

print(min6)
print(max6)