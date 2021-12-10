import random

import basic
from _data import *


class AntiDetecAction():
    
    def __init__(self, windowName):
        '''
        initialization
            :param __window_name__: simulator window name
        '''
        self.ctrl = basic.BasicMethod(windowName)
        
    def randomDrag(self, probability=0.1):
        if random.uniform(0.0, 1.0) <= probability:
            self.ctrl.sceneDrag(DRAG_RANDOM, DRAG_RANDOM)
            
            
    # def hand_mitama(self):

