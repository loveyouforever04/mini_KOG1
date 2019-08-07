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
eq = EQAttack()
our_sol = Soldier(h, eq)
print('\n***我方士兵***', end='')
our_sol.show_me()

# 创建一个敌方士兵
h = Hero()
eq = EQDefense()
enemy = Soldier(h, eq)
print('\n***敌方士兵***', end='')
enemy.show_me()

# 连续交手，至乙方失去战斗力或死亡为止
no_body_lose = True
fight_cnt = 0
while no_body_lose:
    # 交手
    print('\n----------第 %d 次交战---------' % (fight_cnt+1))
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

    # 查看是否有输者
    if our_sol.check_status() != GLV.STATUS_OF_SOLDIER[0]:
        no_body_lose = False
    elif enemy.check_status() != GLV.STATUS_OF_SOLDIER[0]:
        no_body_lose = False
    else:
        no_body_lose = True
        fight_cnt += 1

print('\n*****交战结束，共计交手 %d 次' % (fight_cnt+1))
print('我方士兵 %s 状态： %s' % (our_sol.name, our_sol.check_status()))
print('敌方士兵 %s 状态： %s' % (enemy.name, enemy.check_status()))
