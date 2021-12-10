# -*- coding:utf-8 -*-

import random
import sys
import time

import yaml

sys.path.append('script')
from script.pack import MyClass

with open('_config.yml', 'r', encoding='utf-8')as f:
    cont = f.read()
SET = yaml.safe_load(cont)

MyClass.detect(*SET['detect'])
# MyClass.teamFight(*SET['teamFight'])
ROUNDS = 1
while ROUNDS<4:
    print("\033[0;35;mCURRENT_ROUNDS_START: %s\033[0m" %ROUNDS)
    MyClass.soloWard(*SET['soloWard'])
    
    MyClass.multiExplore(*SET['multiExplore'])
    MyClass.soloWard(*SET['soloWard'])
    
    MyClass.multiMitama(*SET['multiMitama'])
    MyClass.soloWard(*SET['soloWard'])
    
    # MyClass.soloSog(*SET['soloSog'])
    # MyClass.soloWard(*SET['soloWard'])
    
    # MyClass.soloDef(*SET['soloDef'])
    # MyClass.soloWard(*SET['soloWard'])
    print("\033[0;35;mCURRENT_ROUNDS_END: %s\033[0m" %ROUNDS)
    time.sleep(random.randint(1200,1500))
    ROUNDS += 1
