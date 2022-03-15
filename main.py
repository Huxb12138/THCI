import random
import time
import numpy as np


def getstable():
    while True:
        list = []

        list.append(random.randint(0,100))
        time.sleep(1)
        list.append(random.randint(0,100))
        time.sleep(1)
        list.append(random.randint(0,100))
        time.sleep(1)
        list.append(random.randint(0,100))
        time.sleep(1)
        list.append(random.randint(0,100))

        if len(list) == 5:
            medvalue = np.median(list)
            return medvalue
        break


class Basket:
    amount = 0
    level = 0  # 0:a=0 1:a<=30  2:30<a<=70 3:70<a<=80 4:a>80
    cycle = 0
    time_start = 0
    time_end = 0

    def update_amount(self):
        self.amount = getstable()

    def show_amount(self):
        print(self.amount)

    def check_amount(self):
        if self.amount == 0:
            self.level = 0
            print('it is level 0')
        elif self.amount <= 30:
            self.level = 1
            print('it is level 1')
        elif 30 < self.amount <= 70:
            self.level = 2
            print('it is level 2')
        elif self.amount > 70 and self.amount <= 80:
            self.level = 3
            print('it is level 3')
        elif self.amount > 80:
            self.level = 4
            print('it is level 4')
        return self.level

    def check_laundry(self):
        if (self.amount == 0 and self.level != 0):
            self.cycle = self.cycle + 1
            self.time_end = time.time()


    def check_add(self):
        if (self.level == 0 and self.amount != 0):
            self.time_start = time.time()

    def check_time(self):
        time = self.time_end - self.time_start
        if (time >= 100):
            print("Long time no laundry")
        else: print(time)

mybasket = Basket()
while True:
    mybasket.update_amount()
    mybasket.show_amount()
    # time.sleep(5)
    mybasket.check_laundry()

    mybasket.check_add()
    mybasket.check_amount()

print(getstable())
