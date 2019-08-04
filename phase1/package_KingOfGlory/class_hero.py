import random
import sys
sys.path.append('..')
import package_KingOfGlory.global_var as GLV
class Hero():
    def __init__(self):
        '''初始化一个英雄的函数'''
        self.position = random.choice(GLV.TYPE_OF_HERO)
        self.name = self.__set_name__(self.position)
        self.life_force = self.__set_life_force(self.position)

        self.physical_attack = self.__set_physical_attack(self.position)
        self.physical_defense = self.__set_physical_defense(self.position)

        self.mana_power = self.__set_mana_power(self.position)
        self.mana_attack = self.__set_mana_attack(self.position)
        self.mana_defense = self.__set_mana_defense(self.position)

        self.move_speed = self.__set_move_speed(self.position)
        return
 # Public method
    def show_me(self):
        # print('-------------------------------------------------------')
        print('(%s)%s:\t' %
              (GLV.DICT_OF_HERO[self.position], self.name), end='')
        '''
        print('生命=%3d，物攻=%2d，物防=%2d,' % (
            self.life_force, self.physical_attack, self.physical_defense), end='')
        print('法力=%3d，法攻=%2d，法防=%2d,' % (
            self.mana_power, self.mana_attack, self.mana_defense), end='')
        print('速度=%2d' % (self.move_speed))
        '''
        return
# Private method -------------------
    def __set_name__(self, hero_type):

        hero_list = ()
        if hero_type == GLV.TYPE_OF_HERO[0]:
            hero_list = (
                '猪八戒',
                '嫦娥',
                '孙策',
                '梦奇',
                '苏烈',
                '铠',
                '东皇太一',
                '太乙真人',
                '张飞',
                '牛魔',
                '刘邦',
                '程咬金',
                '关羽',
                '项羽',
                '达摩',
                '夏侯惇'
            )
        elif hero_type == GLV.TYPE_OF_HERO[1]:
            hero_list = (
                '曜',
                '盘古',
                '李信',
                '孙策',
                '狂铁',
                '裴擒虎',
                '苏烈',
                '铠',
                '哪吒',
                '雅典娜',
                '杨戬',
                '钟馗',
                '刘备',
                '孙悟空',
                '亚瑟',
                '橘右京',
                '花木兰',
                '韩信',
                '露娜',
                '程咬金',
                '关羽',
                '老夫子',
                '达摩',
                '李白',
                '宫本武藏',
                '典韦',
                '曹操',
                '夏侯惇',
                '吕布',
                '钟无艳',
                '赵云'
            )
        elif hero_type == GLV.TYPE_OF_HERO[2]:
            hero_list = (
                '云中君',
                '上官婉儿',
                '李信',
                '司马懿',
                '元歌',
                '裴擒虎',
                '百里玄策',
                '百里守约',
                '孙悟空',
                '橘右京',
                '娜可露露',
                '不知火舞',
                '花木兰',
                '兰陵王',
                '韩信',
                '貂蝉',
                '李白',
                '阿轲',
                '赵云'
            )
        elif hero_type == GLV.TYPE_OF_HERO[3]:
            hero_list = (
                '嫦娥',
                '上官婉儿',
                '沈梦溪',
                '司马懿',
                '米莱狄',
                '弈星',
                '杨玉环',
                '女娲',
                '梦奇',
                '干将莫邪',
                '诸葛亮',
                '钟馗',
                '不知火舞',
                '张良',
                '王昭君',
                '姜子牙',
                '露娜',
                '安琪拉',
                '貂蝉',
                '武则天',
                '甄姬',
                '周瑜',
                '芈月',
                '扁鹊',
                '孙膑',
                '高渐离',
                '嬴政',
                '妲己',
                '墨子',
                '小乔'
            )
        elif hero_type == GLV.TYPE_OF_HERO[4]:
            hero_list = (
                '伽罗',
                '公孙离',
                '百里守约',
                '黄忠',
                '成吉思汗',
                '虞姬',
                '李元芳',
                '后羿',
                '狄仁杰',
                '马可波罗',
                '鲁班七号',
                '孙尚香'
            )
        else:
            hero_list = ('no-name')
        return random.choice(hero_list)


    def __set_life_force(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的生命力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.8 * GLV.MAX_LIFE_FORCE, 1.0 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_LIFE_FORCE, 0.8 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_LIFE_FORCE, 0.6 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.2 * GLV.MAX_LIFE_FORCE, 0.4 * GLV.MAX_LIFE_FORCE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.1 * GLV.MAX_LIFE_FORCE, 0.2 * GLV.MAX_LIFE_FORCE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value


    def __set_physical_attack(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的物理攻击 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.2 * GLV.MAX_ATTACK, 0.4 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.8 * GLV.MAX_ATTACK, 1.0 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_ATTACK, 0.6 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   #
            value = random.uniform(
                0.01 * GLV.MAX_ATTACK, 0.2 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.6 * GLV.MAX_ATTACK, 0.8 * GLV.MAX_ATTACK)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value


    def __set_physical_defense(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的物理防御 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.8 * GLV.MAX_DEFENSE, 1.0 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_DEFENSE, 0.8 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.2 * GLV.MAX_DEFENSE, 0.4 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.01 * GLV.MAX_DEFENSE, 0.2 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.4 * GLV.MAX_DEFENSE, 0.6 * GLV.MAX_DEFENSE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_power(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.1 * GLV.MAX_MANA_POWER, 0.2 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4* GLV.MAX_MANA_POWER, 0.5 * GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.3* GLV.MAX_MANA_POWER, 0.4* GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.5 * GLV.MAX_MANA_POWER, 1.0* GLV.MAX_MANA_POWER)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_MANA_POWER, 0.3 * GLV.MAX_MANA_POWER)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value


    def __set_move_speed(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的移动速度 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.01 * GLV.MAX_MOVE_SPEED, 0.2 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4 * GLV.MAX_MOVE_SPEED, 0.6 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.8 * GLV.MAX_MOVE_SPEED, 1.0 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.2 * GLV.MAX_MOVE_SPEED, 0.4 * GLV.MAX_MOVE_SPEED)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.6 * GLV.MAX_MOVE_SPEED, 0.8 * GLV.MAX_MOVE_SPEED)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_attack(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法术攻击力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.01 * GLV.MAX_ATTACK, 0.2 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.6 * GLV.MAX_ATTACK, 0.8 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.4 * GLV.MAX_ATTACK, 0.6 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.8 * GLV.MAX_ATTACK, 1.0 * GLV.MAX_ATTACK)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_ATTACK, 0.4 * GLV.MAX_ATTACK)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value

    def __set_mana_defense(self, hero_type):
        ''' 根据英雄类型，随机生成英雄的法术防御力 '''
        value = 0
        if (hero_type == GLV.TYPE_OF_HERO[0]):      # 'TANK': '坦克'
            value = random.uniform(
                0.6 * GLV.MAX_DEFENSE, 0.8 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[1]):   # 'WARRIOR': '战士'
            value = random.uniform(
                0.4 * GLV.MAX_DEFENSE, 0.6 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[2]):   # 'ASSASSIN': '刺客'
            value = random.uniform(
                0.01 * GLV.MAX_DEFENSE, 0.2 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[3]):   # 'MAGE': '法师'
            value = random.uniform(
                0.8 * GLV.MAX_DEFENSE, 1.0 * GLV.MAX_DEFENSE)
        elif (hero_type == GLV.TYPE_OF_HERO[4]):   # 'ARCHER': '射手'
            value = random.uniform(
                0.2 * GLV.MAX_DEFENSE, 0.4 * GLV.MAX_DEFENSE)
        else:                                      # 其他不认可的英雄类型
            value = -1

        return value
