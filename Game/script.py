from random import randint, choice
import time as t
from game_heroes import Hero
from game_weapons import random_weapon
from base_classes import Warrior

orc = Hero(attack_punch=100)
orc.money = 50
orc.name= 'Zloy'
orc.defend = 40


a = Hero()
c = Warrior(health=400,name='Злобный орк', defend=40)
while a.health > 0 and c.health > 0:
    x = randint(0,1)
    if x:
        # t.sleep(2)
        a.attack_counter += 1
        a.attack(c)
        if a.attack_counter == 3:
            a.lvl += 1
            print(f'{a.name} уровен прокачался и равен {a.lvl}')
            count_attack_a = 0
            a.death_in_battle(c)
    else:
        # t.sleep(2)
        c.attack(a)
        count_attack_c += 1
        a.attack(c)
        if count_attack_c == 3:
            c.lvl += 1
            print(f'{c.name} уровен прокачался и равен {c.lvl}')
            count_attack_c = 0