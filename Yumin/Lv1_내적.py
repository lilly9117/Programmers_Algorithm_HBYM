#https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum(x*y for x,y, in zip(a,b))