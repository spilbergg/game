# from random import *
#
# def random_weapon():
#     quality_weapon = ["ordinary", "rare", "improved"]
#     weapon_list = ['Sword', 'Staff', 'Knife', 'Spear', 'Bow', 'Crossbow', 'Axe']
#     quality_random = choice(weapon_list)
#     weapon_random = choice(quality_weapon)
#     print(f"Вам выпал --> {quality_random}  {weapon_random}  если ходите применить его, нажмите 1 если нет, то 0\n")
#     select_weapon = input()
#     for i in weapon_random, quality_random:
#         print(i, end=' ')
#         if select_weapon == "1":
#
#
#
# random_weapon()
c = []
x = True
while x:
    select_weapon = input()
    if select_weapon == '1':
        print('сибо что сделали свой выбор')
        c.append(1)
        x = False
    if select_weapon == '0':
        x = False

    else:
        print("сделайте правильный выбор, 1 иф")


