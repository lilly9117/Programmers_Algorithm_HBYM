#https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    n= list(map(int,str(n)))
    n= ''.join(map(str, sorted(n)[::-1]))
    return int(n)