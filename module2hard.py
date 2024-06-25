number = int(input('введите число от 3 до 20: '))
parol = []
for i in range(1,21):
    for j in range(1,21):
        if number % (i+j) == 0 and i!=j and i<j:
            #print(i,j)
            parol.append(i)
            parol.append(j)

print('искомый код:',*parol)
