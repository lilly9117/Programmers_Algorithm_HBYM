#https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    tmp= (max(a,b)-min(a,b)+1)/2    
    return (a+b)*tmp
