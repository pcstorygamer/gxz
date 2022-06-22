# -*- coding:utf-8 -*-
#
import os

dir = os.getcwd() + "\\发布日志\\publishgame-20211122.log"
file = open(dir,'r',encoding='utf-16')



for i in file.readlines():
    if "开始制作索引" in i:
        stime = i.split(",")[0]
    if "制作机下载索引任务 完成" in i:
        etime = i.split(",")[0]
        name = i.split(",")[1].split("制作机下载索引任务")[0].split(" ")[1]



