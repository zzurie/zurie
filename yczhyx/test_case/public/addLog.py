# -*- coding: utf-8 -*-
#此文档用于添加日志信息
import time

def addLog(logdetail):
    day=time.strftime("%Y-%m-%d")
    now=time.strftime("%Y/%m/%d-%H:%M:%S",time.localtime(time.time()))
    logfile=open("F:\\learn\\yczhyx\\log\\"+day+"-log.txt","a+")
    logfile.write(now+": "+logdetail+"\n")

if __name__=="__main__":
    addLog("测试")