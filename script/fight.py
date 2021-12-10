# -*- coding:utf-8 -*-


import random
import threading
import time

import win32gui

import basic
import scene
from _data import *


class ModeSolo():
    
    def __init__(self, windowName):
        '''
        : param '__window_name_0__':
            str EN only;
            Simulator name
        '''
        self.ctrl = basic.BasicMethod(windowName)
        self.move = scene.SceneChange(windowName)

    # 业原火
    def sogFight(self, all_times = 50, flow_time = 25):
        self.move.toSog()
        self.ctrl.sceneClickOnce(IMG_SGF_LV3)
        current_times = 0
        while current_times < all_times:
            current_times += 1
            self.ctrl.waitImg(IMG_SGF_FIGHT)
            self.ctrl.sceneClickLoseImg(IMG_SGF_FIGHT, IMG_SGF_FIGHT, 3)
            self.move.fightStream(LOC_SGF_BLANK, IMG_SGF_FIGHT,
                                  flow_time)
            if current_times > all_times:
                print('sogenfire_completed')
                return 1
    # 御灵
    def defFight(self, all_times = 50, flow_time = 10):
        self.move.toDef()
        self.ctrl.sceneClickOnce(IMG_DEF_LV3)
        current_times = 0
        while current_times < all_times:
            current_times += 1
            self.ctrl.waitImg(IMG_DEF_FIGHT)
            self.ctrl.sceneClickLoseImg(IMG_DEF_FIGHT,
                                        IMG_DEF_FIGHT, 3)
            self.move.fightStream(LOC_DEF_BLANK, IMG_DEF_FIGHT,
                                  flow_time)
            if current_times > all_times:
                print('palladium_completed')
                return 1
    # 个突
    def warSingleFight(self, sign_option=1):
        self.move.toWar()
        x = 140; y = 70; w = 100; h = 45; x_d = 150; y_d = 60
        time.sleep(1)
        save_cut =   self.ctrl.screenShot()
        record = []
        for i in range(3):
            for j in range(3):
                x_0 = x + i * x_d
                y_0 = y + j * y_d
                x_1 = x_0 + w
                y_1 = y_0 + h
                dst = save_cut[y_0:y_1, x_0:x_1]
                if self.ctrl.discernGive(dst, IMG_WAR_SUCCEED) is None:
                    record.append([i,j])
        del dst, save_cut
        while 1:
            esc_key = 0
            random.shuffle(record)
            print(record)
            for num in range(len(record)):
                if self.ctrl.discernShot(IMG_WAR_RUNOUT_SINGLE) is not None:
                    self.move.yardBack()
                    print('ward_single_completed')
                    return 1
                x_0 = x + record[num][0] * x_d
                y_0 = y + record[num][1] * y_d
                ward_single_loc_border = {'C':[x_0,y_0], 'R': (w, h)}
                while num == len(record) - 1:
                    self.ctrl.waitImg(IMG_WARD_IN)
                    self.ctrl.sceneClickGainImg(ward_single_loc_border, IMG_WAR_FIGHT, 4)
                    self.ctrl.sceneClickOnce(IMG_WAR_FIGHT)
                    self.ctrl.waitImg(IMG_FIGHT_QUIT, REGION_UPPER_LEFT)
                    self.ctrl.sceneClickGainImg(IMG_FIGHT_QUIT,IMG_WAR_QUIR_CONFIRM,
                                                1)
                    self.ctrl.sceneClickOnce(IMG_WAR_QUIR_CONFIRM)
                    self.ctrl.waitImg(IMG_FIGHT_FAIL)
                    self.ctrl.sceneClickGainImg(LOC_WAR_SINGLE_BLANK , IMG_WARD_IN)
                    self.ctrl.waitImg(IMG_WARD_IN)
                    esc_key += 1
                    if esc_key >= random.randint(3, 4):
                        break
                self.ctrl.waitImg(IMG_WARD_IN)
                self.ctrl.sceneClickGainImg(ward_single_loc_border, IMG_WAR_FIGHT , 3)
                self.ctrl.sceneClickOnce(IMG_WAR_FIGHT)
                fail_key = self.move.fightStream(LOC_WAR_SINGLE_BLANK, IMG_WARD_IN,
                                                  5, 1, sign_option, 1, 2)
                self.ctrl.waitImg(IMG_WARD_IN)
                for val in [3, 6, 9]:
                    if num == len(record) + val - 10:
                        self.ctrl.sceneClickGainImg(LOC_WAR_SINGLE_BLANK, IMG_WRD_MEDAL)
                        self.ctrl.sceneClickLoseImg(LOC_WAR_SINGLE_BLANK, IMG_WRD_MEDAL)
                if fail_key == 0:
                    record = list([i,j] for i in range(3) for j in range(3))
                    self.ctrl.sceneClickGainImg(IMG_WAR_REFRESH,
                                         IMG_WAR_REFRESH_CONFIRM)
                    self.ctrl.sceneClickOnce(IMG_WAR_REFRESH_CONFIRM)
                    break
                if num == len(record) - 1:
                    record = list([i,j] for i in range(3) for j in range(3))
                    break
        self.move.yardBack()
    # 寮突
    def warGuildFight(self, sign_option=1):
        while 1:
            self.move.toWar()
            self.ctrl.waitImg(IMG_GUILD)
            self.ctrl.sceneClickGainImg(IMG_GUILD,
                                 IMG_GUILD_IN)
            self.ctrl.waitImg(IMG_WAR_LIAO)
            while 1:
                if self.ctrl.discernShot(IMG_WAR_RUNOUT_GUILD) is not None :
                    self.move.yardBack()
                    print('ward_guild_completed')
                    return 1
                if self.ctrl.discernShot(IMG_WAR_END, REGION_WAR_GUILD_END) is not None :
                    self.move.yardBack()
                    print('ward_guild_completed')
                    return 1
                self.ctrl.sceneClickGainImg(LOC_WAR_GUILE_CHOOSE,
                                            IMG_WAR_FIGHT, 4)
                self.ctrl.sceneClickOnce(IMG_WAR_FIGHT)
                if self.ctrl.discernShot(IMG_WAR_COOLDOWN) is not None :
                    self.move.yardBack()
                    break
                self.move.fightStream(LOC_WAR_SINGLE_BLANK, IMG_WAR_LIAO, 
                                       3, 1, sign_option, 0, 4)
    
class ModeTeam():
    
    def __init__(self, windowName):
        '''
        : param '__window_name_0__':
            str EN only;
            Simulator name
        '''
        self.ctrl = basic.BasicMethod(windowName)
        self.move = scene.SceneChange(windowName)
    # 御魂队员
    def __teamInvitee(self):
        while 1:
            self.move.fightStream(LOC_MITAMA_BLANK, IMG_TEAM_IN, 0)
    # 御魂司机
    def __team_inviter(self): 
        mitama_invitee = self.ctrl.screenShot()[50:62, 285:320]
        while 1:
            self.ctrl.sceneClickLoseImg(IMG_MIT_FIGHT, None, 4)
            self.move.fightStream(LOC_MITAMA_BLANK, mitama_invitee, 1)
            
    def teamFight(self, mode_option=0):
        '''
        '''
        if mode_option:
            self.__team_inviter()
        self.__teamInvitee()
        

class ModeMulti():
    
    def __init__(self, windowName0=None, windowName1=None):
        '''
        : param 'windowName0'/windowName1:
            str EN only;
            Simulator invitee/inviter name
        '''
        self.windowName0 = windowName0
        self.windowName1 = windowName1
        
        self.ctrl_0 = basic.BasicMethod(self.windowName0)
        self.ctrl_1 = basic.BasicMethod(self.windowName1)
        
        self.move_0 = scene.SceneChange(self.windowName0)
        self.move_1 = scene.SceneChange(self.windowName1)
        
        self.event_mitama_first = threading.Event()
        self.event_mitama_finish = threading.Event()
        
        self.event_EXP_join = threading.Event()
        self.event_EXP_quit = threading.Event()
        self.event_EXP_rotate = threading.Event()
        
    def __mitamaInviteeFirst(self):
        self.ctrl_0.waitImg(IMG_MIT_ACCEPT)
        self.ctrl_0.sceneClickOnce(IMG_MIT_ACCEPT)
        time.sleep(2)
        self.event_mitama_first.set()
        self.ctrl_0.waitImg(IMG_FIGHT_PREPARE)
        self.ctrl_0.sceneClickLoseImg(IMG_FIGHT_PREPARE)
        time.sleep(10)
        self.event_mitama_first.clear()
        self.ctrl_0.waitImg(IMG_MIT_WIN)
        self.ctrl_0.sceneClickOnce(LOC_MITAMA_BLANK)
        self.ctrl_0.waitImg(IMG_MIT_COUNT)
        self.ctrl_0.sceneClickLoseImg(LOC_MITAMA_BLANK, IMG_MIT_COUNT)
        self.ctrl_0.waitImg(IMG_MIT_ALWAYS)
        time.sleep(1)
        self.ctrl_0.sceneClickLoseImg(IMG_MIT_ALWAYS, IMG_MIT_ALWAYS)
            
    def __mitamaInviterFirst(self, friend_opt, times):
        self.move_1.teamMake(IMG_TEAM_M, friend_opt)
        self.event_mitama_first.wait()
        # self.mitama_invitee = self.ctrl_1.screen_shot()[50:62, 285:320]
        self.ctrl_1.sceneClickLoseImg(IMG_MIT_FIGHT, None)
        self.ctrl_1.waitImg(IMG_FIGHT_PREPARE)
        self.ctrl_1.sceneClickLoseImg(IMG_FIGHT_PREPARE, None)
        time.sleep(10)
        self.ctrl_1.waitImg(IMG_MIT_WIN)
        self.ctrl_1.sceneClickGainImg(LOC_MITAMA_BLANK, ING_MIT_5)
        time.sleep(0.5)
        self.ctrl_1.sceneClickOnce(LOC_TEAM_MAKE_6)
        time.sleep(0.5)
        self.ctrl_1.sceneClickOnce(ING_MIT_5)
        self.fight_times = random.randint(times, times+5)
    
    # 御魂队员
    def __mitamaInvitee(self):
        for num in range(self.fight_times):
            # print(num,self.fight_times)
            self.event_mitama_finish.set()
            self.move_0.fightStream(LOC_MITAMA_BLANK, IMG_MIT_QUIT, 10, 0,
                                    0,0,3, REGION_UPPER_LEFT)
            print('fight:'+str(num))
            self.event_mitama_finish.clear()
        self.ctrl_0.sceneClickGainImg(LOC_TEAM_MAKE_7,
                                      ING_MIT_5)
        self.ctrl_0.sceneClickLoseImg(ING_MIT_5)
        self.event_mitama_finish.set()
        return 1
    # 御魂司机
    def __mitamaInviter(self): 
        for num in range(self.fight_times):
            # print(num,self.fight_times)
            self.event_mitama_finish.wait()
            self.event_mitama_finish.clear()
            self.ctrl_1.sceneClickLoseImg(IMG_MIT_FIGHT, IMG_TEAM_SCENE)
            self.move_1.fightStream(LOC_MITAMA_BLANK, IMG_MIT_QUIT, 10, 0,
                                    0,0,3, REGION_UPPER_LEFT)
        self.event_mitama_finish.wait()
        time.sleep(1)
        self.ctrl_1.sceneClickGainImg(LOC_TEAM_MAKE_7,
                                      ING_MIT_5)
        self.ctrl_1.sceneClickLoseImg(ING_MIT_5)
        return 1

    def mitamaMultiFight(self, times, friend_opt):
        T_0 = threading.Thread(target=self.__mitamaInviteeFirst,
                               name='mitamaInviteeFirst',
                               )
        T_1 = threading.Thread(target=self.__mitamaInviterFirst,
                               name='mitamaInviterFirst',
                               args=(friend_opt, times,))
        T_0.start()
        T_1.start()
        T_1.join()
        T_0.join()
        T_0 = threading.Thread(target=self.__mitamaInvitee,
                               name='mitamaInvitee',)
        T_1 = threading.Thread(target=self.__mitamaInviter,
                               name='mitamaInviter')
        T_0.start()
        T_1.start()
        T_1.join()
        T_0.join()
        print('mitama_multi_completed')
        
        
    def __exploreFightFlow(self):
        '''
        Explore combat procedures.
        '''
        
        T_0 = threading.Thread(target=self.move_0.fightStream,
                               name='exploreInviteeFlow',
                               args=(LOC_EXP_BLANK, IMG_EXP_AUTO, 0,
                                     0,0,0,
                                     2,REGION_EXP_AUTO))
        T_1 = threading.Thread(target=self.move_1.fightStream,
                               name='exploreInviterFlow',
                               args=(LOC_EXP_BLANK, IMG_EXP_AUTO, 0,
                                     0,0,0,
                                     2,REGION_EXP_AUTO))
        T_0.start()
        T_1.start()
        T_0.join()
        T_1.join()
    def __exploreInvitee(self, fight_times): 
        rotate_check = 1
        for current_times in range(fight_times):
            print('explore_current_times: %s' %(current_times+1))
            self.ctrl_0.waitImg(IMG_EXP_INVITED)
            self.ctrl_0.sceneClickLoseImg(IMG_EXP_ACCEPT)
            self.event_EXP_join.set()
            self.ctrl_0.waitImg(IMG_EXP_INTERFACE)
            if rotate_check:
                if self.ctrl_0.discernShot(IMG_EXP_ROTATE) is not None:
                    self.ctrl_0.sceneClickOnce(LOC_EXP_ROTATE)
                    time.sleep(1)
                rotate_check = 0
                self.event_EXP_rotate.set()
            self.event_EXP_quit.wait()
            self.event_EXP_quit.clear()
            time.sleep(3)
            if self.ctrl_0.discernShot(IMG_EXP_INTERFACE) is not None:
                self.ctrl_0.sceneClickGainImg(IMG_EXP_QUIT,
                                IMG_EXP_QUIT_CONFIRM)
                self.ctrl_0.sceneClickLoseImg(IMG_EXP_QUIT_CONFIRM)
        return 1
    
    def __exploreInviter(self, fight_times=5, friend_opt=0): 
        self.move_1.yardBack()
        self.move_1.teamMake(IMG_TEAM_E, friend_opt)
        rotate_check = 1
        for current_times in range(fight_times):
            self.event_EXP_join.wait()
            self.event_EXP_join.clear()
            self.ctrl_1.sceneClickLoseImg(IMG_EXP_FIGHT)
            self.ctrl_1.waitImg(IMG_EXP_INTERFACE)
            if rotate_check:
                if self.ctrl_1.discernShot(IMG_EXP_ROTATE) is not None:
                    self.ctrl_1.sceneClickOnce(LOC_EXP_ROTATE)
                    time.sleep(1)
                rotate_check = 0
                self.event_EXP_rotate.wait()
                self.event_EXP_rotate.clear()
            while self.ctrl_1.discernShot(IMG_EXP_XX) is None:
                if self.ctrl_1.discernShot(IMG_EXP_X) is not None:
                    time.sleep(0.5)
                    self.ctrl_1.sceneClickLoseImg(IMG_EXP_X)
                    if self.ctrl_1.discernShot(IMG_EXP_INTERFACE) is not None:
                        self.ctrl_1.sceneDrag(DRAG_EXP_RIGHT,
                                              DRAG_EXP_LEFT)
                    else:
                        self.__exploreFightFlow()
                else:
                    self.ctrl_1.sceneDrag(DRAG_EXP_RIGHT,
                                          DRAG_EXP_LEFT)
            time.sleep(0.5)
            self.ctrl_1.sceneClickLoseImg(IMG_EXP_XX)
            self.__exploreFightFlow()
            self.event_EXP_quit.set()
            time.sleep(3)
            if self.ctrl_1.discernShot(IMG_EXP_INTERFACE) is not None:
                self.ctrl_1.sceneClickGainImg(IMG_EXP_QUIT, IMG_EXP_QUIT_CONFIRM)
                self.ctrl_1.sceneClickLoseImg(IMG_EXP_QUIT_CONFIRM)
            self.ctrl_1.waitImg(IMG_EXP_CONTINUE)
            if current_times == fight_times - 1:
                self.ctrl_1.sceneClickLoseImg(IMG_EXP_PAUSE)
                return 1
            self.ctrl_1.sceneClickLoseImg(IMG_EXP_CONTINUE)
            
    def exploreMultiFight(self, fight_times=10, friend_opt=0): 
        '''
        : param fight_times: 
            int>0; Number of fights with boss.
        : param friend_opt:
            '0'/'1'; Friends in the same/other region.
        : param rang_0/rang_1:
            1>float>0; Exp drag distance.
        '''
        T_0 = threading.Thread(target=self.__exploreInvitee,
                                    name='exploreInvitee',
                                    args=(fight_times,),)
        T_1 = threading.Thread(target=self.__exploreInviter,
                                    name='exploreInviter',
                                    args=(fight_times, friend_opt,))
        T_0.start()
        T_1.start()
        T_1.join()
        T_0.join()
        print('explore_multi_completed')

class ModeOther():
    '''
    Provides additional functionality for multithreading
    '''
    def __init__(self, *args):
        '''
        : param args:
            str EN only;
            Simulator name
        '''
        self.members = ()
        for member in args:
            if win32gui.FindWindow(None, member) != 0:
                self.members = self.members + (member,)
                
    def buffSwich(self, window_name, *numbers):
        buff_ctrl = basic.BasicMethod(window_name)
        buff_move = scene.SceneChange(window_name)
        buff_move.yardBack()
        buff_ctrl.sceneClickOnce(IMG_BUFF)
        buff_ctrl.waitImg(IMG_BUFF_BUTTON)
        for val in numbers:
            buff_button = {'C': (380, 64 + (val - 1) * 30), 'R': (35, 4)}
            buff_ctrl.sceneClickOnce(buff_button)
            time.sleep(1)
            del buff_button
        buff_ctrl.sceneClickOnce(IMG_BUFF)
        del buff_ctrl
            
    def sealRefuse(self, fre=5):
        while 1:
            for member in self.members:
                ctrl = basic.BasicMethod(member)
                if ctrl.discernShot(IMG_TASKS) is not None:
                    ctrl.sceneClickLoseImg(LOC_TASK_REFUSE, IMG_TASKS)
                del ctrl
            time.sleep(fre)
            
    def fightCount(self, fre=300):
        initial_time = time.time()
        while 1:
            start = scene.SceneChange.COUNT
            time.sleep(fre)
            current = scene.SceneChange.COUNT
            current_time = time.time()
            print("\033[0;32;mFLOW time: %smin\nstart: %s  current: %s\033[0m" %(int((current_time - initial_time)/60), start, current))
            if start == current:
                pass
                # for member in self.members:
                #     ctrl = basic.BasicMethod(member)
                #     hwnd = ctrl.__hwnd
                #     win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_ESCAPE, 0)
                #     win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_ESCAPE, 0)
            
class TaskQueue():
    def __init__(self, windowName0=None, windowName1=None):
        '''
        : param '__window_name_0__'/__window_name_1__:
            str EN only;
            Simulator invitee/inviter name
        '''
        self.windowName0 = windowName0
        self.windowName1 = windowName1
    
    def thread_start(obj):
        def Threads(*args):
            t = threading.Thread(target=obj, name=obj.__name__, args=args)
            t.start()
        return Threads

    def thread_join(obj):
        def Threads(*args):
            t = threading.Thread(target=obj, name=obj.__name__, args=args)
            t.start()
            t.join()
        return Threads

    def thread_fnc(obj):
        def Threads(*args):
            t = threading.Thread(target=obj, name=obj.__name__, args=args)
            return t
        return Threads
        
    @thread_join
    def soloSogFight(self, *args):
        ModeSolo(self.windowName0).sogFight(*args)

    @thread_join
    def soloDefFight(self, *args):
        ModeSolo(self.windowName0).defFight(*args)
    
    @thread_join
    def soloWardSingle(self, *args):
        ModeSolo(self.windowName0).warSingleFight(*args)
    
    @thread_fnc
    def soloWardSingleSub(self, *args):
        ModeSolo(self.windowName1).warSingleFight(*args)
    
    @thread_join
    def soloWardGuild(self, *args):
        ModeSolo(self.windowName0).warGuildFight(*args)

    @thread_join
    def teamFight(self, *args):
        ModeTeam(self.windowName0).teamFight(*args)
        
    @thread_join
    def multiMitama(self, *args):
        ModeMulti(self.windowName0, self.windowName1).mitamaMultiFight(*args)

    @thread_join
    def multiExplore(self, *args):
        ModeMulti(self.windowName0, self.windowName1).exploreMultiFight(*args)
    
    @thread_start
    def otherRefuseTask(self, fre):
        ModeOther(self.windowName0, self.windowName1).sealRefuse(fre)
    
    @thread_start
    def otherFightCount(self, fre):
        ModeOther(self.windowName0).fightCount(fre)
    
if __name__ == '__main__':
    test = TaskQueue('sub')
    test.otherRefuseTask(1)
    # test.other_fight_count_p(3)

