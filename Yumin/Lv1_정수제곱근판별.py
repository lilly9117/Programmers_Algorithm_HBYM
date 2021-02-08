#https://programmers.co.kr/learn/courses/30/lessons/12934

import math
def solution(n):
    tmp = math.sqrt(n)
    return (tmp+1)**2 if int(tmp)==tmp else -1