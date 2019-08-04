
import random
import sys
sys.path.append('..')
import package_KingOfGlory.global_var as GLV
from package_KingOfGlory.class_equipment import Equipment

class EQMana(Equipment):


    add_mana_attack=0.0
    def __init__(self):
        self.name=self.__set_name()
        for i in range(GLV.MAX_FORCE_TIMES):
            n=random.randint(0,10)
            self.__forge__eq(n)
        return
    def show_me_unique(self):
        print('-----独有加成-----')
        print('      法术攻击+%2d' % (self.add_mana_attack))
        print('-----------------')
        return

    def __set_name(self):

        all_eq_name = (
            '咒术典籍',
            '蓝宝石',
            '炼金护符',
            '圣者法典',
            '元素杖',
            '大棒',
            '破碎圣杯',
            '光辉之剑',
            '魅影面罩',
            '进化水晶',
            '血族之书',
            '炽热支配者'
            '梦魇之牙',
            '虚无法杖',
            '博学者之怒'
            '辉月',
            '回响之杖',
            '冰霜法杖',
            '痛苦面具',
            '巫术法杖',
            '圣杯',
            '时之预言',
            '贤者之书',
            '噬神之书'
        )

        return random.choice(all_eq_name)
    def __forge__eq(self,skill_num):
        if skill_num==5:
            self.add_life_force+=0.05*GLV.MAX_LIFE_FORCE
        if skill_num==6:
            self.add_mana_power+=0.05*GLV.MAX_MANA_POWER
        if skill_num==9:
            self.add_mana_attack+=0.05*GLV.MAX_ATTACK
        if skill_num==3:
            self.restore_mana_power+=0.05*GLV.MAX_MANA_POWER
        if skill_num==4:
            self.add_move_speed+=0.05*GLV.MAX_MOVE_SPEED
        pass
        return
