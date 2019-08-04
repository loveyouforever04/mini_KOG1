
# -*- coding: UTF-8 -*-
import random
import sys
sys.path.append('..')
import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_equipment import Equipment
class EQDefense(Equipment):
    restore_life_force=0.0
    def __init__(self):
        self.name=self.__set_name()
        for i in range(GLV.MAX_FORCE_TIMES):
            n=random.randint(0,10)
            self.__forge_eq(n)
        return

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +回血:%0.2f' % (self.restore_life_force))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '红玛瑙',
            '布甲',
            '抗魔披风',
            '提神水晶',
            '力量腰带',
            '熔炼之心',
            '神隐斗篷',
            '雪山圆盾',
            '守护者之铠',
            '反伤刺甲',
            '血魔之怒',
            '红莲斗篷',
            '霸者重装',
            '不祥征兆',
            '不死鸟之眼',
            '魔女斗篷',
            '极寒风暴',
            '冰痕之握',
            '护贤者的庇护',
            '暴烈之甲'
        )

        return random.choice(all_eq_name)



    def __forge_eq(self,skill_num):
        '''锻造道具'''
        if skill_num==0:
            self.add_physical_attack+=0.05*GLV.MAX_ATTACK
        elif skill_num==1:
            self.add_physical_defense+=0.05*GLV.MAX_DEFENSE
        elif skill_num==2:
            self.add_mana_defense+=0.05*GLV.MAX_DEFENSE
        elif skill_num==3:
            pass
        elif skill_num==4:
            pass
        elif skill_num==5:
            self.add_life_force+=0.05*GLV.MAX_LIFE_FORCE
        elif skill_num==6:
            self.add_mana_power+=0.05*GLV.MAX_MANA_POWER
        elif skill_num==7:
            pass
        elif skill_num==8:
            pass
        elif skill_num==9:
            pass
        elif skill_num==10:
            self.restore_life_force=random.uniform(0.1,0.5)
            if self.restore_life_force>=0.5:
                self.restore_life_force=0.5
            pass
        return
