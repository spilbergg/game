# import time
#
#
# def decorat(fn):
#     def wr():
#         print('Евгений ложится спать')
#         time.sleep(4)
#         fn()
#         print('Ты усё проспал')
#     return wr
#
#
# @decorat
# def some():
#     print('Евгений')
#
#
# some()


#
# a = [x for x in range(10)]
# b = (x for x in range(10))
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())
# print(b.__next__())

#
# def countdouwn(num):
#     z = 2+2+num
#     print(z, '32')
#     yield z
#     x = 5+5+num
#     print(x, '35')
#     yield x
#     y = 10+10+num
#     print(y, '38')
#     yield y

# a = countdouwn(100)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# class Bissnes:
#     b = jija
#     def __init__(self, jija):
#         self.jija = jija
#
#     def __iter__(self):
#         return self

''' запросы по сети '''
# import time

# import requests
# import re


# data = requests.get('https://jsonplaceholder.typicode.com/users/1')
# print(data.json())
# print(data)
# print(data.text)
# print(type(data.json()))
#
# lst = ['http://127.0.0.1:8000/market/', 'https://jsonplaceholder.typicode.com/users/1', 'https://jsonplaceholder.typicode.com/posts']
#
# def send_request(arr):
#     for site in arr:
#         data = requests.get(site)
#         yield data
#
# data1 = send_request(lst)
# print(data1.__next__().text)
# print(data1.__next__().text)
# print(data1.__next__().text)
# print(data1.__next__().text)

#
# def fn():
#     try:
#         print(data1.__next__().text)
#         time.sleep(2)
#         print('подождали 2 секунды')
#         print(f'получим пользователя {data1.__next__().text}')
#         time.sleep(5)
#         print(f'Получим все посты {data1.__next__().text}')
#     except StopIteration:
#         print('все зпросы сделаны')
#
# fn()
import random

''' регулярные выражения '''
# def reg(x):
#     if re.findall(r'\d', x):
#         print('есть цифры')
#     else:
#         print('no цифры')
# reg('adaasfdaD12')
''' регулярка на проверку номера телефона '''
# def reg1(x):
#     if re.match(r'\+375\(29\)...\-..\-..', x):
#         print('yes')
#     else:
#         print('no')
# reg1('+375(29)666-46-05')

''' генератор функции '''

#
#
# import sqlite3
#
#
# sql1 = '''
#     insert INTO market_30_category (name) values ('Какао')
# '''
# sql2 = '''
#     insert INTO market_30_category (name) values ('getara')
# '''
# sql3 = '''
#     insert INTO market_30_category (name) values ('garmon')
# '''
#
#
# def counter(x, y, z):
#     connect = sqlite3.connect('db.sqlite3')
#     cursor = connect.cursor()
#     cursor.execute(x)
#     connect.commit()
#     g = cursor.execute('SELECT * FROM market_30_category')
#     p = g.fetchall()
#     cursor.close()
#     yield print(f'записалось ок {p}')
#
#
#     connect = sqlite3.connect('db.sqlite3')
#     cursor = connect.cursor()
#     cursor.execute(y)
#     connect.commit()
#     g = cursor.execute('SELECT * FROM market_30_category')
#     p = g.fetchall()
#     cursor.close()
#     yield print(f'записалось ок {p}')
#
#
#     connect = sqlite3.connect('db.sqlite3')
#     cursor = connect.cursor()
#     cursor.execute(z)
#     connect.commit()
#     g = cursor.execute('SELECT * FROM market_30_category')
#     p = g.fetchall()
#     cursor.close()
#     yield print(f'записалось ок {p}')
#
#
# result = counter(sql1, sql2, sql3)
#
# result.__next__()
# result.__next__()
# result.__next__()
# print(10//10)


import time

'''декоратор подсчёта времени'''


# def time_argument(times):
#     def decorator_limit(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             time.sleep(times)
#             return result
#         return wrapper
#     return decorator_limit
# @time_argument(10)
# def func():
#     print('ушел в сон')
#     return 'вернулся'
#
# x = func()
# print(x)
#
#
# def time_setaup(times):
#     def time_sleep_los(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             time.sleep(times)
#             return result
#         return wrapper
#     return time_sleep_los
#
#
# @time_setaup(int(input('время для сна')))
# def fn():
#     print('лось лёг спать')
#     return 'лось проснулся'
#
# x = fn()
# print(x)

# def fib(x):
#     # if x in (1, 2):
#     #     return 1
#     if x == 1:
#         return 1
#     if x == 0:
#         return 0
#     else:
#         return fib(x-1) + fib(x-2)
#
# z = fib(10)
# print(z)
#
# fib1 = fib2 = 1
# print(fib1,fib2, end='')
# n = int(input())
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


# def num_fib(x):
#     if x == 1:
#         return 1
#     elif x == 0:
#         return 0
#     else:
#         return num_fib(x-1) + num_fib(x-2)
# x = num_fib(int(input()))
# print(x)

#
# def factorial(x=int(input())):
#     if x == 0:
#         return 1
#     else:
#         return factorial(x - 1) * x
#
#
# z = factorial()
#
# print(z)

# def is_palindron(num):
#     if num//10 == 0:
#         return False
#     temp = num
#     revers_num = 0
#     while temp != 0:
#         revers_num = (revers_num*10)+ temp%10
#         temp = temp//10
#
#     if num == revers_num:
#         return True
#     else:
#         return False
#
# def __iter__(self):
#     return self
#
#
# def __next__(self):
#     a = self.name[self.index]
#
#     if self.index < len(self.name):
#         self.index += 1
#     else:
#         iter(self.name)
#         self.index = 0
#     return a

from random import *
import time as t

class Warrior:
    def __init__(self, weapon, health=300, lvl=1, damage=20, name='Unknown', defend=10):
        self.weapon = weapon
        self.health = health
        self.lvl = lvl
        self.damage = damage
        self.name = name
        self.defend = defend

    def attack(self, other):
        rand = randint(0, 1)
        if rand:
            other.health -= self.damage
            if other.health <= 0:
                print(f'{other.name} умер')
                print('игра закончилась')
            else:
                print(f'{self.name} наносит удар, {other.name} ранен, у противника осталось {other.health} здоровья')
        else:
            self.defender(other)

    def defender(self, other):
        if other.lvl == self.lvl:
            print(f'{self.name} отразил удар')
        elif other.lvl > self.lvl:
            random_attack = randint(15, 20)
            self.health -= random_attack + self.defend
            print(f'уровень {other.name} больше твоего, получай ответный урон ==> {x} ! остаток здоровья {self.name} = {self.health}')
        else:
            other.health -= self.damage + other.defend

    def up_lvl(self, other):
        if self:
            self.lvl += 1
            self.health += 55
            self.defend += 5
        else:
            other.lvl += 1
            other.health += 55
            other.defend += 5

    def change_weapon(self, other):
        if self:
            Weapon().drop_weapon()



class Weapon:
    def __init__(self, name, enhancement, damage, sword=25, axe=30, knife=20, spear=40):
        # super().__init__()
        self.name = name
        # self.__initiate_weapon()
        self.sword = sword
        self.axe = axe
        self.knife = knife
        self.spear = spear
        self.enhancement = enhancement
        self.damage = damage

    def __initiate_weapon(self):
        all_weapons = choice(["knife", "sword", "axe", "spear"])

        quality = choice(["ordinary", "rare", "improved"])
        if quality == "ordinary":
            self.name = quality
            self.weapon_strength = 30
            self.damage = 30
            print(f'Вам выпало оыбчное оружие с прочностю {self.weapon_strength} и атакой {self.damage}')
        if quality == "rare":
            self.name = quality
            self.weapon_strength = 50
            self.damage = 40
            print(f'Вам выпало редкое оружие с прочностю {self.weapon_strength} и атакой {self.damage}')
        if quality == "improved":
            self.name = quality
            self.weapon_strength = 70
            self.damage = 50
            print(f'Вам выпало улучшеное оружие с прочностю {self.weapon_strength} и атакой {self.damage}\n '
                  f'хотите ли вы его привенить? да - 1, нет -2 ')
            x = int(input('\n'))
            if x:
                Warrior().weapon = self.



        if self.name == "knife":
            quality = choice(["ordinary", "rare", "improved"])
            if
        elif self.name == "sword":
            quality = "Rare"
            weapon_strength = 50
            damage = 56
        elif self.name == "axe":
            quality = "Rare"
            weapon_strength = 20
            damage = 30
        else:
            if self.name == "spear":
                quality = "Rare"
                weapon_strength = 20
                damage = 30


    def drop_weapon(self):
        # не надо
        # super().drop_weapon()
        if Warrior().self.lvl ==  2:
            self.damage = self.knife
        elif self.lvl == 3 or 4:
            random_weapon = [self.axe, self.sword]
            self.damage = random.choice(random_weapon)
        else:
            self.damage = self.spear


# a = Warrior(name=input('Имя\n'), health=300)
a = Weapon()
c = Warrior(name='player2', health=300)




count_attack_a = 0
count_attack_c = 0
while a.health > 0 and c.health > 0:
    x = randint(0,1)
    if x:
        # t.sleep(2)
        count_attack_a += 1
        a.attack(c)
        if count_attack_a == 3:
            a.lvl += 1
            print(f'{a.name} уровен прокачался и равен {a.lvl}')
            count_attack_a = 0
            a.
    else:
        # t.sleep(2)
        c.attack(a)
        count_attack_c += 1
        a.attack(c)
        if count_attack_c == 3:
            c.lvl += 1
            print(f'{c.name} уровен прокачался и равен {c.lvl}')
            count_attack_c = 0


# ALL_WEAPONS = ["knife", "sword", "axe"]
# def get_weapons():
#     weapons = list()
#     for weapon_name in ALL_WEAPONS:
#         weapons.append(Weapon(weapon_name))
#
#     return weapons
#
# weapons = get_weapons()
#
#
# def change_weapon(self, new_weapon):
#     if self.level_is_okay():
#         self.weapon = new_weapon


"""
1. Главный персонаж - воин -> создаем 2 объекта воина и ими деремся. Аттрибуты:
защита,
атака,
уровень,
имя,
оружие,
здоровье.

Методы:
атаковать,
защищаться,
повысить уровень,
сменить оружие(новое оружие)


2. У воина есть оружие (класс), должен иметь атрибуты:
прочность,
заточка,
урон.

Методы:
сломаться -> урон от него 0
починить -> возвращает урон
"""
