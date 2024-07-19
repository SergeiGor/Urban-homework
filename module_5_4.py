class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

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


    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            print('ошибка')

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        else:
            print('ошибка')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        else:
            print('ошибка')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        else:
            print('ошибка')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        else:
            print('ошибка')

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('ошибка')

    def __radd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('ошибка')

    def __iadd__(self, value):
        if isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        elif isinstance(value, int):
            self.number_of_floors += value
            return self
        else:
            print('ошибка')

    def __del__(self):
        print(f"<{self.name}> снесён, но он останется в истории")





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)