grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dic={}
students2 = sorted(students)
print("студенты по алфвиту:",students2)
n=len(students2)
print("всего студентов:",n)
for i in range(0,n):
    name = students2[i]
    print("студент",name,grades[i])
    sr=sum(grades[i])/len(grades[i]) #средний бал
    print("средний бал",sr)
    dic[name]=sr

print()
print("итоговый словарь:",dic)


