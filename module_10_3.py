import random
import time
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            value = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += value
            print (f'Пополнение: {value}. Баланс: {self.balance}. ')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            value = random.randint(50, 500)
            print(f'Запрос на снятие: {value}. ')
            if value <= self.balance:
                self.balance -= value
                print (f'Снятие: {value}. Баланс: {self.balance}. ')
                time.sleep(0.001)
            else:
                print('Запрос отклонен, недостаточно средств.')
                time.sleep(0.001)
                self.lock.acquire()



bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
