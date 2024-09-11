from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"<{self.name}, на нас напали!")
        count = 100
        day =0
        while count > 0:
            count -= self.power
            day += 1
            if count < self.power:
                count = 0
            print(f'{self.name}, сражается {day} дня (день)..., осталось {count} воинов')
            sleep(1)
        print(f'{self.name}, одержал победу спустя {day} дня (день)')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все бытвы закончились!')