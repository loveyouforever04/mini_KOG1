import random
import sys
sys.path.append('..')
import package_KingOfGlory.global_var as GLV

print('\n-----cutting line-------')
value = random.randint(0.8*GLV.MAX_LIFE_FORCE,GLV.MAX_LIFE_FORCE)
print(value)
