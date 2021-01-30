#https://programmers.co.kr/learn/courses/30/lessons/12901

import datetime
from datetime import date

def solution(a, b):
    day =['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day[datetime.date(2016,a,b).weekday()]