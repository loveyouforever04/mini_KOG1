
import random
import sys

sys.path.append('..')

import package_KingOfGlory.global_var as GLV

from package_KingOfGlory.class_eq_attack import EQAttack
from package_KingOfGlory.class_eq_move import EQMove
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_soldier import Soldier

h = Hero()
eq=EQAttack()
s = Soldier(h,eq)
s.show_me()

h = Hero()
eq=EQDefense()
s = Soldier(h,eq)
s.show_me()

h = Hero()
eq=EQMana()
s = Soldier(h,eq)
s.show_me()

h = Hero()
eq=EQMove()
s = Soldier(h,eq)
s.show_me()
