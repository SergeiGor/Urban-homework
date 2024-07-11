class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print ('Название:',self.name,', этажей:',self.number_of_floors)
        print()

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






h1 = House('ЖК Горский', 18)
h1.go_to(5)

h2 = House('Домик в деревне', 2)
h2.go_to(10)