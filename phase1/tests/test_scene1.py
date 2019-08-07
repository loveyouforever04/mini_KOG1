# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
#   创建两个士兵交战场面
# ------------------------(max to 80 columns)-----------------------------------


import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV

from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_soldier import Soldier

from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_move import EQMove


print('\n----------交战前---------')
# 创建一个我方士兵
h = Hero()
eq = EQMove()
our_sol = Soldier(h,eq)
print('\n***我方士兵***', end='')
our_sol.show_me()

# 创建一个敌方士兵
h = Hero()
eq = EQMana()
enemy = Soldier(h,eq)
print('\n***敌方士兵***', end='')
enemy.show_me()

# 仅一次交手，测试交战逻辑是否正确
print('\n----------交战一次---------')
if our_sol.move_speed > enemy.move_speed:
    print('\n----------交战中：攻击方的变化---------')
    our_sol.attack()
    print('\n----------交战中：被攻击方的变化---------')
    enemy.be_attacked(our_sol)
else:
    print('\n----------交战中：攻击方的变化---------')
    enemy.attack()
    print('\n----------交战中：被攻击方的变化---------')
    our_sol.be_attacked(enemy)

print('\n----------交战后---------')
enemy.show_me()
our_sol.show_me()
