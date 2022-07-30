# from Game.weapon_quality import rare, improved
from base_classes import Warrior, Weapons
from game_weapons import random_weapon
from random import *
import time as t


class Hero(Warrior):
    def __init__(self, attack_counter=0, attack_punch=5):
        super().__init__(lvl=1, health=300, name='Unknown', defend=10, money=0)
        self.attack_counter = attack_counter
        self.attack_punch = attack_punch

    ''' Атака на моба '''

    def attack(self, other):
        rand = bool(randint(0, 1))
        if rand:
            other.health -= self.weapon.damage  #дамаге это атрибут оружия --урон оружия
            self.attack_counter += 1
            if self.attack_counter % 5 == 0:
                self.up_lvl()
            if other.health <= 0:
                print(f'{other.name} умер')
                print('игра закончилась')
            else:
                print(f'{self.name} наносит удар, {other.name} ранен, у противника осталось {other.health} здоровья')
        else:
            other.defend(self)

    '''Защита от атаки'''

    def defender(self, other):
        if other.lvl == self.lvl:
            print(f'{self.name} отразил удар')
        elif other.lvl > self.lvl:
            random_attack = randint(15, 20)
            self.health -= random_attack + self.defend
            print(f'уровень {other.name} больше твоего, получай ответный урон ==> {random_attack} ! остаток здоровья {self.name} = {self.health}')
        else:
            other.health -= self.weapon + other.defend
            self.attack_counter += 1
            if self.attack_counter % 5 == 0:
                self.up_lvl()

    ''' поднятие уровня '''

    def up_lvl(self):
        if self.lvl < 10:
            self.lvl += 1
            self.health += 55
            self.defend += 5

    ''' бабло с моба '''




    def death_in_battle(self, other):
        self.money += other.money
        if True:
            self.weapon = random_weapon()
            print(f"Ура вам выпало новое оружие{self.weapon}, хотите его забрать? 1-да, 0-нет\n")
            x = True
            while x:
                select_weapon = input()
                if select_weapon == '1':
                    self.add_weapon(self.weapon)
                if select_weapon == '0':
                    x = False

                else:
                    print("сделайте правильный выбор")


    def add_weapon(self, another_weapon):
        if len(self.weapon) < 2:
            self.weapon.append(another_weapon)
            # return True
            print(len(self.weapon),self.weapon[0])
        else:
            print(len(self.weapon))
            print('Вы не можете взять оружие, рюкзак переполнен')
            print('Хотите выбросить какое-нибудь оружие? 1-да, 0-нет')
            # x = True
            while True:
                remove_weapons = str(input())
                if remove_weapons == "1":
                    print(self.add_weapon(self.weapon))
                    self.add_weapon(self.weapon)
                    print('1 if')
                    print(type(self.weapon))
                    for i in self.weapon:
                        print(i)
                    break
                if remove_weapons == '0':
                    # x = False
                    break
                else:
                    print("сделайте правильный выбор")
            return False


c = Hero()

b = random_weapon
a = Hero.add_weapon(c, b)





