# -*- coding:utf-8 -*-


import random
import time

import cv2
import numpy as np
import win32api
import win32con
import win32gui
import win32ui

from _data import *


# Basic running function.
class BasicMethod():
    # app = QApplication(sys.argv)
    def __init__(self, windowName):
        '''
        initialization
            :param __window_name__: simulator window name
        '''
        
        self.windowName = windowName
        self.HWDN = win32gui.FindWindow(None, self.windowName)
        self.hwnd = win32gui.FindWindowEx(self.HWDN,None,None,None)
        self.left, self.top, right, bottom = win32gui.GetWindowRect(self.hwnd)
        self.width = right - self.left
        self.height = bottom - self.top

        self.displayStaus = 0
        self.threshold = 0.85
        
        
        
    def screenPostrue(self):
        exStyle = win32api.GetWindowLong(self.HWDN, win32con.GWL_EXSTYLE)
        win32gui.SetWindowLong (self.HWDN, win32con.GWL_EXSTYLE,
                                exStyle | win32con.WS_EX_LAYERED )
        win32gui.SetLayeredWindowAttributes(self.HWDN, win32api.RGB(0,0,0),
                                            self.displayStaus, win32con.LWA_ALPHA)
        self.displayStaus = 255
        
    def screenShot(self, screen_loc=None):
        '''Return screenshots as RGB data.'''
        while 1:
            try:
                hwndDC = win32gui.GetWindowDC(self.hwnd)
                mfcDC = win32ui.CreateDCFromHandle(hwndDC)
                saveDC = mfcDC.CreateCompatibleDC()
                saveBitMap = win32ui.CreateBitmap()
                saveBitMap.CreateCompatibleBitmap(mfcDC, self.width, self.height)
                saveDC.SelectObject(saveBitMap)
                saveDC.BitBlt((0, 0), (self.width, self.height), mfcDC, (0, 0), win32con.SRCCOPY)
                signedIntsArray = saveBitMap.GetBitmapBits(True)
                img = np.frombuffer(signedIntsArray, dtype='uint8')
                img.shape = (self.height, self.width, 4)
                win32gui.DeleteObject(saveBitMap.GetHandle())
                mfcDC.DeleteDC()
                saveDC.DeleteDC()
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                if screen_loc is not None:
                    img = cv2.resize(img,(640,320))
                    return img[int(screen_loc['C'][1]):int(screen_loc['R'][1])+int(screen_loc['C'][1]),
                               int(screen_loc['C'][0]):int(screen_loc['R'][0])+int(screen_loc['C'][0])]
                return cv2.resize(img,(640,320))
            except:
                print("\033[0;31;mscreen_shot_no_return\033[0m")
                pass
            
    def tempMatching(self, image, templ):
        w, h = templ.shape[::-1]
        res = cv2.matchTemplate(image, templ, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > self.threshold:
            result = {}
            result['C'] = max_loc
            result['R'] = (w, h)
            result['P'] = max_val
            return result

    def tempMatchingAll(self, image, templ):
        w, h = templ.shape[::-1]
        res = cv2.matchTemplate(image, templ, cv2.TM_CCOEFF_NORMED)
        
        loc = np.where(res >= self.threshold)
        result = {}
        for val in zip(*loc[::-1]):
            result.setdefault('C', []).append(val)
        if len(result):
            result['R'] = (w, h)
            result['N'] = len(result['C'])
            return result
        else:
            result['N'] = 0
            return result
        
    # Identify the location of the 'template_graph' and output 'template_graph' in the 'self.save_graph'.
    def discernShot(self, template_graph, screen_loc=None):
        # print(str(template_graph))
        target_graph = self.screenShot(screen_loc)
        if isinstance(template_graph, str):
            template_graph = cv2.imread(template_graph, 0)
        result = self.tempMatching(target_graph, template_graph)
        if result is not None and screen_loc is not None:
            result['C'] = (result['C'][0] + screen_loc['C'][0],
                           result['C'][1] + screen_loc['C'][1])
        return result
          
    def discernGive(self, target_graph, template_graph):
        '''Give the 'template_graph', identify the 'template_graph', and the output 'template_graph' in the 'target_graph' position.'''
        if isinstance(target_graph, str) and isinstance(template_graph, str):
            result = self.tempMatching(cv2.imread(target_graph, 0), cv2.imread(template_graph, 0))
        elif isinstance(template_graph, str):
            result = self.tempMatching(target_graph, cv2.imread(template_graph, 0))
        else:
            result = self.tempMatching(target_graph, template_graph)
        return result

    # Identify the location of the 'template_graph' in the 'self.target_graph' and mark it as a 'draw_graph'. (Test function, none-used)
    def discrenDraw(self, target_graph, template_graph, draw_graph):
        target_graph = cv2.imread(target_graph, 0)
        template_graph = cv2.imread(template_graph, 0)
        result = self.tempMatching(target_graph,template_graph)
        if result is not None:
            cv2.rectangle(target_graph, result['C'],
                          (result['C'][0] + result['R'][0],
                           result['C'][1] + result['R'][1]),
                          (0, 0, 255), 2)
            cv2.imwrite(draw_graph, target_graph)

    # Wait for the 'template_graph' to appear.
    def waitImg(self, template_graph, screen_loc=None):
        while self.discernShot(template_graph, screen_loc) is None:
            self.waitRadom(1)
        return 1
    
    # Wait for the 'template_graph' to disappear.
    def loseImg(self, template_graph, screen_loc=None):
        while self.discernShot(template_graph, screen_loc) is not None:
            self.waitRadom(1)
        return 1
    
    # Wait for two pictures that are not all None to appear.
    def waitImgAll(self, *args):
        while 1:
            for lens in range(len(args)):
                if self.discernShot(args[lens]) is not None:
                    return lens
            self.waitRadom(1)
    
    # Drag from 'start_position' to 'end_position'
    def sceneDrag(self, start_position, end_position):
        self.left, self.top, __right, __bot = win32gui.GetWindowRect(self.hwnd)
        self.width = __right - self.left
        self.height = __bot - self.top
        start_position = (int((start_position['C'][0] + random.uniform(0,start_position['R'][0]))/640*self.width),
                          int((start_position['C'][1] + random.uniform(0,start_position['R'][1]))/320*self.height))
        end_position = (int((end_position['C'][0] + random.uniform(0,end_position['R'][0]))/640*self.width),
                        int((end_position['C'][1] + random.uniform(0,end_position['R'][1]))/320*self.height))
        print("\033[0;31;m%s_drag(%s,%s)\033[0m" %(self.windowName, start_position, end_position))
        v_x = (end_position[0] - start_position[0])/200
        v_y = (end_position[1] - start_position[1])/200
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, 0,win32api.MAKELONG(start_position[0],start_position[1]))
        times = 0
        while times < 200:
            times += 1
            x_m = start_position[0] + v_x * times
            y_m = start_position[1] + v_y * times
            win32api.SendMessage(self.hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON,win32api.MAKELONG(int(x_m),int(y_m)))
            time.sleep(0.3/200)
        win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(int(x_m),int(y_m)))
        time.sleep(0.5)
        
    # Single click 'click_position'
    def sceneClickOnce(self, click_position):
        self.left, self.top, __right, __bot = win32gui.GetWindowRect(self.hwnd)
        self.width = __right - self.left
        self.height = __bot - self.top
        if isinstance(click_position, str):
            click_position = self.discernShot(click_position)
        try:
            loc_x = int((click_position['C'][0] + random.uniform(0,click_position['R'][0]))/640*self.width)
            loc_y = int((click_position['C'][1] + random.uniform(0,click_position['R'][1]))/320*self.height)
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(loc_x, loc_y))
            time.sleep(random.uniform(0.05,0.1))
            win32api.SendMessage(self.hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(loc_x, loc_y))
            print("\033[0;31;m%s_click(%d,%d)\033[0m" %(self.windowName, loc_x, loc_y))
        except:
            print("\033[0;31;mclick_once_pass\033[0m")
            pass

    def sceneClickGainImg(self, click_position, template_graph, rank = 1, screen_loc=None):
        if isinstance(click_position, str):
            click_position = self.discernShot(click_position)
        while 1:
            if self.discernShot(IMG_SCENE) is not None or self.discernShot(template_graph, screen_loc) is not None:
                return 1
            self.sceneClickOnce(click_position)
            self.waitRadom(rank)
                # print('click_location(%d,%d)' %(loc_x,loc_y))
            
    # Click on the 'click_position' area to identify the 'template_graph' until 'template_graph' identifies it as None
    def sceneClickLoseImg(self, click_position, template_graph = None, rank = 1, screen_loc=None): 
        if isinstance(click_position, str):
            if template_graph is None:
                template_graph = click_position
        while 1:
            if self.discernShot(template_graph, screen_loc) is None:
                return 1
            self.sceneClickOnce(click_position)
            self.waitRadom(rank)
            
    # Pause by level 'rank'
    def waitRadom(self, rank):
        if rank == 1:
            time.sleep(random.uniform(0.40, 0.60))
        elif rank == 2:
            time.sleep(random.uniform(0.40, 0.80))
        elif rank == 3:
            time.sleep(random.uniform(0.40, 1.20))
        elif rank == 4:
            time.sleep(random.uniform(0.40, 2.00))

if __name__ == '__main__':
    test = BasicMethod('main')
    # print(test.discernShot('img\war\ward_in.png'))
    cv2.imwrite('fight.png', test.screenShot())
    # while 1:
    #     cv2.imshow('look', test.screen_shot())
    #     cv2.waitKey(10)
