import random
import sys

sys.path.append('..')

from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_move import EQMove
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana


print('\n---测试生成一个攻击类道具---')
test_eq = EQAttack()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---测试生成一个移动类道具---')
test_eq = EQMove()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---测试生成一个防御类道具---')
test_eq = EQDefense()
test_eq.show_me()
test_eq.show_me_unique()

print('\n---测试生成一个法术类道具---')
test_eq = EQMana()
test_eq.show_me()
test_eq.show_me_unique()
