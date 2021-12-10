import time

from fight import ModeOther, TaskQueue
from scene import SceneChange


class MyClass:

    def teamFight(user0, option_team=0):
        TaskQueue(user0).teamFight(option_team)
        
    def detect(user0, user1, fre_refuse=3, fre_fight=300):
        TaskQueue(user0, user1).otherRefuseTask(fre_refuse)
        TaskQueue(user0, user1).otherFightCount(fre_fight)

    def soloWard(user, set=[0,0], option = 2):
        SceneChange(user).presetReplace(*set)
        if option ==2:
            TaskQueue(user).soloWardGuild()
            timeStart = time.time()
            TaskQueue(user).soloWardSingle()
            timeEnd = time.time()
            if timeEnd - timeStart > 360:
                TaskQueue(user).soloWardGuild()
        elif option ==1:
            TaskQueue(user).soloWardGuild()
        elif option ==0:
            TaskQueue(user).soloWardGuild()

    def mutilWard(user0, user1, preset0=[0, 0], preset1=[0, 0]):
        SceneChange(user1).presetReplace(*preset1)
        ward_single_sub = TaskQueue(user1).soloWardSingleSub()
        ward_single_sub.start()
        MyClass.soloWard(user0, preset0)
        if ward_single_sub.is_alive():
            ward_single_sub.join()

    def multiExplore(user0, user1, times = 10, explore_set = None,
                     buff_number0 = None, buff_number1 = None,
                     friend_opt = 0):
        SceneChange(user0).presetReplace(*explore_set)
        if user0 is not None:
            ModeOther().buffSwich(user0, *buff_number0)
        if user1 is not None:
            ModeOther().buffSwich(user1, *buff_number1)
        TaskQueue(user0, user1).multiExplore(times, friend_opt)
        if user0 is not None:
            ModeOther().buffSwich(user0, *buff_number0)
        if user1 is not None:
            ModeOther().buffSwich(user1, *buff_number1)

    def multiMitama(user0, user1, times = 10, mitama_set = None,
                    buff_number0 = None, buff_number1 = None, friend_opt = 0):
        SceneChange(user0).presetReplace(*mitama_set)
        if user0 is not None:
            ModeOther().buffSwich(user0, *buff_number0)
        if user1 is not None:
            ModeOther().buffSwich(user1, *buff_number1)
        TaskQueue(user0, user1).multiMitama(times, friend_opt)
        if user0 is not None:
            ModeOther().buffSwich(user0, *buff_number0)
        if user1 is not None:
            ModeOther().buffSwich(user1, *buff_number1)
            
    def soloDef(user, preset, times, sleep):
        SceneChange(user).presetReplace(*preset)
        TaskQueue(user).soloDefFight(times, sleep)
        
    def soloSog(user, preset, times, sleep):
        SceneChange(user).presetReplace(*preset)
        TaskQueue(user).soloSogFight(times, sleep)
