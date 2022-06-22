# -*- coding:utf-8 -*-


import os
import datetime


#今天如果不是周5无法运行
today = datetime.datetime.now().weekday()
#设置获取时间段
end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:59', '%Y-%m-%d%H:%M')
start_time = end_time + datetime.timedelta(days=-8) + datetime.timedelta(hours=24)+datetime.timedelta(minutes=1)


dir = "D:\\lwserver\\log"
# dir = os.getcwd() + "\\境内日志"
a = datetime.datetime.now().date()
week = open(str(a) + "境内汇总" +".txt",'w')
if os.path.isdir(dir):
    for file in os.listdir(dir):
        log = dir +"\\" + file
        if os.path.isfile(log):
            # a = os.path.getmtime(log)
            # aa = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))
            # if str(start_time) < aa < str(end_time):
            if "lwgamemgr" in log:
                rfile = open(log, 'r', encoding='UTF-16')
                txt = open(file, "w")
                for i in rfile.readlines():
                    if "download complete" in i:
                        bbb = i.replace("download complete, update total:","")
                        ccc = bbb.replace("[","")
                        ddd = ccc.replace("]",",")
                        eee = ddd.replace("MB","")
                        txt.writelines(eee.split(",")[1] +eee.split(",")[2])
                        week.writelines(eee.split(",")[1] +eee.split(",")[2])

#

