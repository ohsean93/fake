'''
#수학 모듈
import math

print("math.radians(90) = {0}".format(math.radians(90)))

print("math.ceil(3.2) = {0}".format(math.ceil(3.2)))
print("math.floor(3.2) = {0}".format(math.floor(3.2)))

print("math.pi = {0}".format(math.pi))
print("math.pi = {0}".format(math.pi))


#import math as m   #모둘을 간단히

#from math import *  #전체 호출
#from math import 함수  #부분 호춯

# 시스탬 모듈
import sys

print("sys.argv => {0} {1}".format(type(sys.argv),sys.argv))

for i, val in enumerate(sys.argv):
    print("sys.argv[{0}] => {1}".format(i,val))
'''

'''
#난수 모듈
from random import random, uniform, randrange, choice, choices, sample, shuffle

print("random() => {0}".format(random()))

print("uniform({0}, {1}) => {2}".format( 1 , 10 , uniform(1.0,10.0) ))

#초기값randrange 함수 stqrt = 0 step = 1

start, stop, step = 1, 45, 2

print("randrange({0}, {1}) => {2}".format(start, stop, randrange(start,stop)))
print("randrange({0}) => {1}".format( stop, randrange(stop)))  
print("randrange({0}, {1}, {2}) => {3}".format(start, stop, step, randrange(start,stop,step)))

# choice choices sample 1개, 복원 비복원

data_list = range(1,6)
print("choice({0}) => {1}".format(data_list,choice(data_list)))
print("choices({0}) => {1}".format(data_list,choices(data_list,k=2)))
print("sample({0}) => {1}".format(data_list,sample(data_list,k=2)))

print("shuffle({0}) => {1}".format(data_list,shuffle(data_list)))

'''

'''
#시간 모듈

from datetime import datetime, timezone, timedelta

now = datetime.now()
print("{0}-{1:02}-{2:02}-{3:02}-{4:02}-{5:02}".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

fmt = "%Y{0}, %m{1}, %d{2}, %H{3}, %M{4}, %S{5}"
print(now.strftime(fmt).format(*"년월일시분초"))
'''
'''
#서드파티 모듈 설치 창에 직접 입력
#pip install pytz
#pip uninstall pytz

from datetime import datetime
from pytz import common_timezones, timezone, utc

#타임존 정보 출력
for tz in list(common_timezones):
    if tz.lower().find("paris")>=0:
        print(tz)

tz_utc = timezone("utc.zone")
tz_seoul = timezone("Asia/Seoul")
tz_paris = timezone("Europe/Paris")

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

now_utc = datetime(tz_utc)
print(now_utc.strftime(fmt))


now_seoul = datetime(tz_seoul)
print(now_seoul.strftime(fmt))


'''

'''
a=1
'''

