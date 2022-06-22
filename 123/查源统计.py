# -*- coding:utf-8 -*-

import os
import datetime
import time


dir = os.getcwd() + "\\查源"
a = datetime.datetime.now().date()
week = open(str(a) + "查源" +".txt",'w')
if os.path.isdir(dir):
    for file in os.listdir(dir):
        log = dir +"\\" + file
        if os.path.isfile(log):
            a = os.path.getmtime(log)
            # if str(start_time) < aa < str(end_time):
            rfile = open(log, 'r', encoding='UTF-16')
            txt = open(file, "w")
            for i in rfile.readlines() :
                sum = int(i.split(",")[4])+int(i.split(",")[5])

                txt.writelines(i.split(",")[1]+":" + i.split(",")[2] +":"+ str(sum) + "\n")
                week.writelines(i.split(",")[1]+":" + i.split(",")[2] +":"+ str(sum) + "\n")



