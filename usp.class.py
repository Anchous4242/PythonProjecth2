#1

import random
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} каже: Привіт!")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} гавкає: Гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав-гав !")


a = Animal("Тварина")
a.speak()

d = Dog("Джек")
d.speak()

class Cat(Animal):  # Dog наслідує Animal
    def speak(self):
        print(f"{self.name} Мяукае: МЯУУУУУУУУУУУУУУУУУУУУУУ!")


a = Animal("Тварина")
a.speak()

c = Cat("Сара")
c.speak()

#2
#import random
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def age(self):
        print(f"{self.name} має {self.age} років.")


class Voditel(Person):
    def __init__(self, name, age, n_p):
        super().__init__(name, age)
        self.n_p = n_p
    def info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")
        print(f"Водійське посвідчення №: {self.n_p}")

random_age = random.randint(20, 40)
v = Voditel("Санечка", random_age, "BC42425252")
v.info()

#3
#import random

class TZ:
    def __init__(self, speed):
        self.speed = speed

    def going(self):
        print(f"Транспорт рухається зі швидкістю {self.speed} км/год.")

class Car(TZ):
    def going(self):
        print(f"Автомобіль їде зі швидкістю {self.speed} км/год.")

class Train(TZ):
    def going(self):
        print(f"Потяг їде зі швидкістю {self.speed} км/год.")

class Bus(TZ):
    def going(self):
        print(f"Автобус їде зі швидкістю {self.speed} км/год.")

car_speed = random.randint(0, 140)
train_speed = random.randint(0, 400)
bus_speed = random.randint(0, 100)

car1 = Car(car_speed)
train1 = Train(train_speed)
bus1 = Bus(bus_speed)

car1.going()
train1.going()
bus1.going()

#4
class Pristriy:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} увімкнено.")
        else:
            print(f"{self.name} вже увімкнено.")

    def off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} вимкнено.")
        else:
            print(f"{self.name} вже вимкнено.")

class TV(Pristriy):
    pass

class PC(Pristriy):
    pass

class Fr(Pristriy):
    pass

tv1 = TV("Телевізор Samsung")
pc1 = PC("Ноутбук Asus")
fr1 = Fr("Холодильник Pro Max")

tv1.on()
tv1.off()

pc1.on()
fr1.off()