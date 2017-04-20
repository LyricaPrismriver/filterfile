#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, math

class itimer:
    #初始化时开始计时
    def __init__(self):
        self.__startime = time.clock()
    #用于调试
    def setTime(self, newTime):
        self.__startime = newTime
    #从当前位置开始计时
    def setStart(self):
        self.__startime = time.clock()
    #获取时长,单位second
    def getSec(self):
        return time.clock() - self.__startime
    #获取时长,格式'HH:MM:SS'
    def getCompleteTime(self):
        delay = self.getSec()
        hours = math.floor(delay / 3600)
        minutes = math.floor((delay % 3600) / 60)
        seconds = delay % 60
        return '%d:%d:%.4f' % (hours, minutes, seconds)
        
