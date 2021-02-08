#https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    tmp = n**(1/2)
    return (tmp+1)**2 if int(tmp)==tmp else -1

#math 모듈 없이 풀기