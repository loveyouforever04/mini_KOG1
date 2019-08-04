
import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_equipment import Equipment

class EQMove(Equipment):

    def __init__(self):
        self.name = self.__set_name()
        for i in range(GLV.MAX_FORCE_TIMES):
            n = random.randint(0,10)
            self.__forge_eq(n)

        return

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       无        ')
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '神速之靴',
            '影忍之足',
            '抵抗之靴',
            '冷静之靴',
            '秘法之靴',
            '急速战靴',
            '疾步之靴'
        )

        return random.choice(all_eq_name)

    def __forge_eq(self, skill_num):
        '''锻造道具'''
        if skill_num == 0:
            pass
        if skill_num == 1:
            pass
        if skill_num == 2:
            self.add_physical_defense += 0.05 * GLV.MAX_DEFENSE
        if skill_num == 3:
            pass
        if skill_num == 4:
            pass
        if skill_num == 5:
            self.add_mana_defense += 0.05 * GLV.MAX_DEFENSE
        if skill_num == 6:
            self.add_move_speed += 0.05 * GLV.MAX_MOVE_SPEED
        if skill_num == 7:
            self.add_mana_power += 0.05 * GLV.MAX_MANA_POWER
        if skill_num == 8:
            pass
        if skill_num == 9:
            pass
        if skill_num == 10:
            pass
        return
