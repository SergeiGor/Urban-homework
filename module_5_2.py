class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # print ('Название:',self.name,', этажей:',self.number_of_floors)
        # print()

    def go_to(self,new_floor):
        if new_floor in range(1,self.number_of_floors):
            print('Этаж',new_floor,'существует, поехали!')
            i=1
            inew_floor = int(new_floor)

            while i <= inew_floor:
                print(i)
                i+=1
            print()
        else:
            print('Этажа',new_floor,'нет')


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return 'название: ' + str(self.name) + ', число этажей:'+ str(self.number_of_floors)





h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print()
print(len(h1))
print(len(h2))
