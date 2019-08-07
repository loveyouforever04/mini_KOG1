
import random
import sys

sys.path.append('..')
from package_machines.mach_maring import pick_a_full_name
from package_KingOfGlory.class_hero import Hero
from package_KingOfGlory.class_eq_mana import EQMana
from package_KingOfGlory.class_eq_defense import EQDefense
from package_KingOfGlory.class_eq_move import EQMove
from package_KingOfGlory.class_eq_attack import EQAttack
import package_KingOfGlory.global_var as GLV

class Soldier():

    def __init__(self, h, *arg):
        eq = arg[0]
        self.__mortal_name = pick_a_full_name()
        self.__clone_from = h.name
        self.__position = h.position
        self.__weapon_name = eq.name

        self.__life_force = h.life_force + eq.add_life_force
        self.__mana_power = h.mana_power + eq.add_mana_power
        self.__move_speed = h.move_speed + eq.add_move_speed

        self.__physical_attack = h.physical_attack + eq.add_physical_attack
        self.__physical_defense = h.physical_defense + eq.add_physical_defense

        self.__mana_defense = h.mana_defense + eq.add_mana_defense
        self.__restore_mana = eq.restore_mana_power

        # 仅部分道具有的特殊技能
        self.__critical_strik = 0.0
        self.__physical_suck = 0.0
        self.__mana_attack = 0
        self.__restore_life_force = 0.0

        if type(eq) is EQAttack:
            self.__weapon_type = 'gongji'
            self.__critical_strik = eq.critical_strik
            self.__physical_suck = eq.physical_suck
        elif type(eq) is EQDefense:
            self.__weapon_type = 'fangyu'
            self.__restroe_life_force = eq.restore_life_force
        elif type(eq) is EQMana:
            self.__weapon_type = 'fashu'
            self.__mana_attack = h.mana_attack + eq.add_name_attack
        elif type(eq) is EQMove:
            self.__weapon_type = 'yidong'
        else:
            pass
            print('daojuleixingcuowu')
        return
        # 显示士兵自身所有信息

    def show_me(self):
        print('\n-----士兵的最新状态-----')
        # print('\n-----只读（不会变化的）属性-----')
        print('士兵姓名:%s\t' % (self.name), end='')
        print('士兵定位:%s(%s)\t' %
              (self.position, GLV.DICT_OF_HERO[self.position]), end='')
        print('士兵武器:%s(%s)' % (self.weapon_name, self.__weapon_type))
        # print('\n-----只读（会变化的）属性-----')
        # print('\n**随着战争而变化的能力，以下为当前数值*')
        print('生命值=%3d\t' % (self.cur_life_force), end='')
        print('法力值=%3d\t' % (self.cur_mana_power), end='')
        print('物防力=%3d\t' % (self.cur_physical_defense), end='')
        print('法防力=%3d' % (self.cur_mana_defense))

        # print('\n**不变的固有能力（所有士兵都具备的能力）**')
        print('物攻力=%3d\t' % (self.physical_attack), end='')
        print('法攻力=%3d\t' % (self.mana_attack), end='')
        print('移动速度=%3d' % (self.move_speed))

        # print('\n**不变的固有能力（依靠道具才具备的能力）**')
        print('暴击率=%0.2f\t' % (self.critical_strik), end='')
        print('物理吸血=%0.2f\t' % (self.physical_suck), end='')
        print('回血=%0.2f\t' % (self.restore_life_force), end='')
        print('回蓝=%0.2f' % (self.restore_mana))

        return

    @property
    def name(self):
        dict = {self.__mortal_name: self.__clone_from}
        return dict

    @property
    def position(self):
        return self.__position

    @property
    def weapon_name(self):
        return self.__weapon_name

    @property  # 移动速度（不变）
    def move_speed(self):
        return self.__move_speed

    @property  # 物理攻击力（不变）
    def physical_attack(self):
        return self.__physical_attack

    @property  # 法术攻击力（不变）
    def mana_attack(self):
        return self.__mana_attack

    @property  # 回蓝%（不变）
    def restore_mana(self):
        return self.__restore_mana

    @property  # 暴击率%（不变）
    def critical_strik(self):
        return self.__critical_strik

    @property  # 物理吸血%（不变）
    def physical_suck(self):
        return self.__physical_suck

    @property  # 回血%（不变）
    def restore_life_force(self):
        return self.__restore_life_force
        # 定义士兵类的只读（可变）属性 ----------------------------

    @property  # 当前生命力
    def cur_life_force(self):
        return self.__life_force

    @property  # 当前生命力
    def cur_mana_power(self):
        return self.__mana_power

    @property  # 物理防御力（可变）
    def cur_physical_defense(self):
        return self.__physical_defense

    @property  # 法术防御力（可变）
    def cur_mana_defense(self):
        return self.__mana_defense
        # 定义士兵类的行为 ----------------------------

    def check_status(self):
        sta = ''
        if self.cur_life_force <= 0:
            sta = GLV.STATUS_OF_SOLDIER[2]  # 已经死亡
        elif self.cur_life_force <= 0.05 * GLV.MAX_LIFE_FORCE:
            sta = GLV.STATUS_OF_SOLDIER[1]  # 苟活状态，无力再战
        else:
            sta = GLV.STATUS_OF_SOLDIER[0]  # 健康状态，可以继续战斗
        return sta
    def attack(self):
        print('--debug: %s 开始发动攻击' % self.name)
        # 只有健康状态才能攻击
        if self.check_status() == GLV.STATUS_OF_SOLDIER[0]:
            # 仅当剩余法力>10%且有法攻时，才能发起法力攻击，消耗 10% 最大法力
            if (self.cur_mana_power > 0.1 * GLV.MAX_MANA_POWER) and (self.mana_attack > 0):
                print('--debug: %s 法力足够发动法术攻击' % self.name)
                self.__mana_power -= GLV.MAX_MANA_POWER * 0.1
                print('--debug: 法术攻击后消耗：法力降为 %d ' % self.__mana_power)
                # 考虑装备的回蓝
                if self.restore_mana > 0:
                    self.__mana_power += self.__mana_power * self.restore_mana
                    print('--debug: 法术攻击后回蓝：法力升为 %d ' % self.__mana_power)

            # 如果能发起物理攻击，则需消耗生命力
            if (self.physical_attack > 0) and (self.cur_life_force > 0.1 * GLV.MAX_LIFE_FORCE):
                print('--debug: %s 体力足够发动物理攻击' % self.name)
                self.__life_force -= GLV.MAX_LIFE_FORCE * 0.05
                print('--debug: 物理攻击消耗后：生命力降为 %d ' % self.__life_force)
                # 如果有回血技能则恢复点生命力
                if self.restore_life_force > 0:
                    self.__life_force += self.__life_force * self.restore_life_force
                # 如果有物理吸血技能则恢复点生命力
                if self.physical_suck > 0:
                    self.__life_force += self.physical_suck * self.physical_attack
                    print('--debug: 物理攻击后回血：生命力升为 %d ' % self.__life_force)

            # 每次攻击都伴随着移动，攻击方要消耗 3% 最大生命力
            self.__life_force -= GLV.MAX_LIFE_FORCE * 0.01
            print('--debug: 移动后消耗：生命力降为 %d ' % self.__life_force)
            self.__move_speed *= 0.9  # 攻击方的速度额外下降 10%
            print('--debug: 移动后移动速度降为 %d ' % self.__move_speed)

        return
        # 声明必须是被另外一个士兵攻击

    def be_attacked(self, enemy):
        # 只有健康状态才能承受攻击
        if self.check_status() == GLV.STATUS_OF_SOLDIER[0]:
            # 当敌人具备法术攻击力，且敌人法力>10% 时才遭受法术攻击
            if (enemy.mana_attack > 0) and (enemy.cur_mana_power > GLV.MAX_MANA_POWER * 0.1):
                print('--debug: %s 遭受 %s 的法术攻击' % (self.name, enemy.name))
                # 承受法术攻击
                if self.cur_mana_defense > 0:
                    print('--debug: 有 %d 的法防' % (self.cur_mana_defense))
                    self.__mana_defense -= GLV.MAX_DEFENSE * 0.3
                    print('--debug: 受法攻后法防降为 %d ' % (self.__mana_defense))
                    self.__life_force -= enemy.mana_attack * 0.3
                    print('--debug: 受法攻后生命力降为 %d ' % (self.__life_force))
                else:
                    self.__life_force -= enemy.mana_attack
                    print('--debug: 无法防，受攻击后生命力降为 %d ' % (self.__life_force))

            # 当敌人具备物理攻击力，且敌人生命力>10% 时才遭受物理攻击
            if enemy.physical_attack > 0 and enemy.cur_life_force > GLV.MAX_LIFE_FORCE * 0.1:
                print('--debug: %s 遭受 %s 的物理攻击' % (self.name, enemy.name))
                # 承受物理攻击
                if self.cur_physical_defense > 0:
                    print('--debug: 有 %d 的物防' % (self.cur_physical_defense))
                    self.__physical_defense -= GLV.MAX_DEFENSE * 0.3  # 削弱物防力
                    print('--debug: 受物攻后物防降为 %d ' % (self.__physical_defense))
                    # 要考虑对方的物攻-暴击率影响
                    if enemy.critical_strik > 0:
                        if random.random() < enemy.critical_strik:
                            # 对方暴击生效，受到双倍打击
                            self.__life_force -= enemy.physical_attack * 0.6
                            print('--debug: 敌方暴击生效，受物攻后生命力降为 %d ' %
                                  (self.__life_force))
                        else:
                            self.__life_force -= enemy.physical_attack * 0.3
                            print('--debug: 敌方有暴击但无效，受物攻后生命力降为 %d ' %
                                  (self.__life_force))
                    else:
                        self.__life_force -= enemy.physical_attack * 0.3
                        print('--debug: 无暴击，受物攻后生命力降为 %d ' %
                              (self.__life_force))
                else:
                    print('--debug: 没有物防')
                    if enemy.critical_strik > 0:
                        if random.random() < enemy.critical_strik:
                            # 对方暴击生效，受到双倍打击
                            self.__life_force -= enemy.physical_attack * 2
                            print('--debug: 敌方暴击生效，受物攻后生命力降为 %d ' %
                                  (self.__life_force))
                        else:
                            self.__life_force -= enemy.physical_attack * 1
                            print('--debug: 敌方有暴击但无效，受物攻后生命力降为 %d ' %
                                  (self.__life_force))
                    else:
                        self.__life_force -= enemy.physical_attack * 1
                        print('--debug: 无暴击，受物攻后生命力降为 %d ' %
                              (self.__life_force))

            # 每次攻击都伴随着移动，被攻击方要消耗 3% 最大生命力
            self.__life_force -= GLV.MAX_LIFE_FORCE * 0.03
            print('--debug: 移动后消耗：生命力降为 %d ' % self.__life_force)

        else:
            print('--debug: %s 生命力为 %d，已经死亡 ' % (self.name, self.__life_force))

        return
