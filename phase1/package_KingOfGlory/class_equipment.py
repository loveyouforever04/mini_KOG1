import random
import sys

sys.path.append('..')
import package_KingOfGlory.global_var as GLV

class Equipment():

    name = ''

    sale_price = 0
    buy_price = 0

    add_physical_attack = 0
    add_physical_defense = 0

    add_mana_defense = 0
    restore_mana_power = 0   # 回蓝

    add_move_speed = 0

    add_life_force = 0
    add_mana_power = 0

    def __init__(self):
        ''' 初始化一个道具类
            在父类中初始化不赋值
        '''
        pass
        return

    def show_me(self):
        print('-----名称价格-----')
        print('道具名称:%s' % (self.name))
        #print('售价(出售价):%5d' % (self.sale_price))
        #print('总价(采购价):%5d' % (self.buy_price))
        print('-----通用加成-----')
        print('     物理攻击+%3d' % (self.add_physical_attack))
        print('     物理防御+%3d' % (self.add_physical_defense))
        print('     法术防御+%3d' % (self.add_mana_defense))
        print('        回蓝+%0.2f' % (self.restore_mana_power))
        print('     移动速度+%3d' % (self.add_move_speed))
        print('     最大生命+%3d' % (self.add_life_force))
        print('     最大法力+%3d' % (self.add_mana_power))
        return
