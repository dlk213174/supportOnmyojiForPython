# -*- coding:utf-8 -*-


import glob
import random
import time

import anti
import basic
from _data import *


class SceneChange():
    COUNT = 0
    
    def __init__(self, windowName1):
        '''
        initialization
            :param __window_name__: simulator window name
        '''
        self.ctrl = basic.BasicMethod(windowName1)
        self.safe = anti.AntiDetecAction(windowName1)
    
    def fightStream(self, clickPosition, finalImg, flowTime = 10, 
                    preOption = 0, signOption = 0, out_option = 0, 
                    rank = 2, screen_loc = None):
        SceneChange.COUNT += 1
        self.ctrl.waitImg(IMG_FIGHT_QUIT, REGION_UPPER_LEFT)
        print('FIGHT_START')
        if preOption:
            self.ctrl.waitImg(IMG_FIGHT_ENTER)
            self.ctrl.sceneClickLoseImg(LOC_FIGHT_PREPARE, IMG_FIGHT_ENTER)
        if signOption:
            self.ctrl.sceneClickOnce(LOC_FIGHT_SIGN)
        time.sleep(1)
        self.safe.randomDrag()
        time.sleep(flowTime)
        self.ctrl.loseImg(IMG_FIGHT_QUIT, REGION_UPPER_LEFT)
        time.sleep(1)
        print('FIGHT_COUNT')
        if out_option:
            result =  self.ctrl.waitImgAll(IMG_FIGHT_FAIL, IMG_FIGHT_WIN)
            self.ctrl.sceneClickGainImg(clickPosition, finalImg)  # img_scene
            return result
        if self.ctrl.discernShot(finalImg) is None:
            self.ctrl.sceneClickGainImg(clickPosition, finalImg, rank, screen_loc)  # img_scene
        print('FIGHT_END')
        return 1
    
    # 从任意不含需要二次确定的位置回到庭院界面
    def yardBack(self):
        escGraphs = glob.glob(SCE_PATH + '*).png')
        while 1:
            if self.ctrl.discernShot(IMG_SELF) is not None:
                time.sleep(2)
                return 1
            for item in escGraphs:
                if self.ctrl.discernShot(item) is not None:
                    self.ctrl.sceneClickLoseImg(item, item, 2)
                    
    # 打开卷轴
    def scrollOpen(self):
        scrollStaus = self.ctrl.waitImgAll(IMG_SCROLL_ON, IMG_SCROLL_OFF)
        if scrollStaus:
            self.ctrl.sceneClickOnce(IMG_SCROLL_OFF)
            self.ctrl.waitImg(IMG_SCROLL_ONALL)
            return 1
        else:
            return 1


    # 关闭卷轴
    def scrollClose(self):
        scrollStaus = self.ctrl.waitImgAll(IMG_SCROLL_OFF, IMG_SCROLL_ON)
        if scrollStaus:
            self.ctrl.sceneClickLoseImg(IMG_SCROLL_ON, IMG_SCROLL_ONALL)
            return 1
        else:
            return 1
    
    # 进入式神录
    def toList(self):
        self.ctrl.waitImg(IMG_SHIKIGAMI)
        self.ctrl.sceneClickLoseImg(IMG_SHIKIGAMI,
                             IMG_SHIKIGAMI, 2)
        while self.ctrl.discernShot(IMG_PRESET_0) is None:
            self.ctrl.waitRadom(1)
        # print('to_list')
        return 1
    
   # 进入探索地图
    def toExplore(self):
        self.yardBack()
        self.ctrl.sceneClickOnce(LOC_EXP_ENTER)
        time.sleep(1)
        if self.ctrl.discernShot(IMG_SELF) is not None:
            self.scrollOpen()
            self.ctrl.sceneClickLoseImg(IMG_SCENE_EARTHLY, IMG_SCENE_EARTHLY, 4)
            self.yardBack()
            self.ctrl.sceneClickLoseImg(LOC_EXP_ENTER, IMG_SELF, 4)
        # print('to_explore')
        return(1)

    # 去哪里？
    def toWhere(self, where):
        while self.ctrl.discernShot(SCE_PATH + str(where) + '.png') is None:
            self.ctrl.waitRadom(1)
        # print('find%s' %(str(where)))
        self.ctrl.sceneClickLoseImg(SCE_PATH + str(where) + '.png',
                             SCE_PATH + str(where) + '.png', 3)
        # print('reach%s' %(str(where)))
        return(1)
        
    # 前往业原火
    def toSog(self):
        self.toExplore()
        self.toWhere('mitama')
        self.toWhere('sogenfire')
        # print('to_sogenfire')
        return(1)

    # 前往御灵
    def toDef(self):
        self.toExplore()
        self.toWhere('defender')
        for i in range(4):
            self.ctrl.sceneClickOnce(LOC_DEF[i])
            self.ctrl.waitRadom(3)
            if self.ctrl.discernShot(IMG_DEFENDER_0) is None:
                # print('to_palladium')
                return(1)
            if i == 3:
                # print('fail_to_palladium')
                return(0)
            
    # 前往突破
    def toWar(self):
            self.toExplore()
            self.toWhere('ward')
            
    # 更换预设
    def presetReplace(self, presetGroup=0, presetNumber=0):
        if int(presetNumber) == 0:
            # print('no_need')
            return 1
        else:
            self.yardBack()
            self.scrollOpen()
            self.toList()
            while self.ctrl.discernShot(IMG_PRESET_5) is None:
                self.ctrl.waitRadom(2)
            self.ctrl.waitRadom(2)
            self.ctrl.sceneClickOnce(IMG_PRESET_0)
            while self.ctrl.discernShot(IMG_PRESET_1) is None:
                self.ctrl.waitRadom(2)
            self.ctrl.sceneClickOnce(LOC_PRESET_GROUP[int(presetGroup)])
            self.ctrl.waitRadom(2)
            for i in range(random.randint(2,4)):
                self.ctrl.sceneClickOnce(LOC_PRESET_NUMBER[int(presetNumber)])
                self.ctrl.waitRadom(2)
            if self.ctrl.discernShot(IMG_PRESET_2) is not None:
                self.ctrl.sceneClickOnce(IMG_PRESET_2)
                # print('succeed')
                self.yardBack()
                return 1
            self.yardBack()
    
    def teamMake(self, where, friendStaus):
        '''
        args:
            friend_key:
                    'defult': 'Friends in the same region.'
                    'else': 'Friends in the other region.'
        '''
        self.yardBack()
        self.scrollOpen()
        self.ctrl.waitImg(IMG_TEAM_MAKE)
        self.ctrl.sceneClickLoseImg(IMG_TEAM_MAKE)
        self.ctrl.waitImg(IMG_TEAM_INTERFACE)
        time.sleep(0.5)
        for t in range(2):
            self.ctrl.sceneDrag(DRAG_TEAM_TOP,
                                DRAG_TEAM_BOT)
            time.sleep(0.5)
        time.sleep(0.5)
        while self.ctrl.discernShot(where) is None:
            self.ctrl.sceneDrag(DRAG_TEAM_BOT,
                                DRAG_TEAM_TOP)
            time.sleep(0.5)
        self.ctrl.sceneClickOnce(where)
        time.sleep(0.5)
        for t in range(3):
            self.ctrl.sceneDrag(DRAG_TEAM_CHAPTER_BOT,
                                DRAG_TEAM_CHAPTER_TOP)
            time.sleep(0.5)
        self.ctrl.sceneClickOnce(LOC_TEAM_CHPYER)
        time.sleep(0.5)
        self.ctrl.sceneClickGainImg(LOC_TEAM_CREAT,
                             IMG_TEAM_CREAT)
        self.ctrl.waitImg(IMG_TEAM_CREAT)
        time.sleep(1)
        self.ctrl.sceneClickOnce(LOC_TEAM_PRIVATE)
        time.sleep(1)
        self.ctrl.sceneClickOnce(IMG_TEAM_CREAT)
        self.ctrl.waitImg(IMG_TEAM_INVITE_INTERFACE)
        time.sleep(1)
        self.ctrl.waitImg(IMG_TEAM_ADD)
        self.ctrl.sceneClickGainImg(IMG_TEAM_ADD,
                             IMG_TEAM_INVITE, 4)
        time.sleep(2)
        if friendStaus == 1:
            self.ctrl.sceneClickOnce(IMG_TEAM_FRIEND_TRANS)
            self.ctrl.sceneClickOnce(IMG_TEAM_FRIEND_TRANS)
        else:
            self.ctrl.sceneClickOnce(IMG_TEAM_FRIEND_LOCAL)
            self.ctrl.sceneClickOnce(IMG_TEAM_FRIEND_LOCAL)
        self.ctrl.sceneClickGainImg(LOC_TEAM_FIREDN_FIRST,
                             IMG_TEAM_FRIEND_INVITED)
        self.ctrl.sceneClickLoseImg(IMG_TEAM_INVITE)


if __name__ == '__main__':
    test = SceneChange('阴阳师 - 星云引擎')
    test.yardBack()
