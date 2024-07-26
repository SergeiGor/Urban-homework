class Animal:
    def __init__(self,name):
        self.name = name
    alive = True
    fed = False
class Predator(Animal):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print (self.name,'получил', food.name)
        print('Сеъдобность -', food.edible)
        if food.edible:
            self.fed = True
            print(self.name, 'съел', food.name)
        else:
            self.alive = False
            print(self.name,'не стал есть',food.name)

class Mammal(Animal):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print (self.name,'получил', food.name)
        print('Сеъдобность -', food.edible)
        if food.edible:
            self.fed = True
            print(self.name, 'съел', food.name)
        else:
            self.alive = False
            print(self.name, 'не стал есть', food.name)


class Plant:
    def __init__(self,name):
        self.name = name
    edible = False

class Flower(Plant):
    def __init__(self,name):
        self.name = name

class Fruit(Plant):
    def __init__(self,name):
        self.name = name
    edible = True




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)