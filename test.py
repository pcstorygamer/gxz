# -*- coding:utf-8 -*
import time
import datetime


# #白开始时间
# start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:00', '%Y-%m-%d%H:%M')
# #白结束时间
# end_time = start_time+datetime.timedelta(hours=+13)+datetime.timedelta(minutes=-1)
# # 当前时间
# now_time = datetime.datetime.now()
# #夜开始时间
# n_start_time = end_time+datetime.timedelta(minutes=+1)
# #夜结束时间
# n_end_time = n_start_time+datetime.timedelta(hours=+11)+datetime.timedelta(minutes=-1)

#
# print( n_start_time < now_time < n_end_time )

while True:
    # 白开始时间
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '7:00', '%Y-%m-%d%H:%M')
    # 白结束时间
    end_time = start_time + datetime.timedelta(hours=+13) + datetime.timedelta(minutes=-1)
    # 当前时间
    now_time = datetime.datetime.now()
    print(now_time)
    if start_time < now_time < end_time:
        time.sleep(10)
    else:
        time.sleep(20)