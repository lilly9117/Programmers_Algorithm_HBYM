#https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    return "".join(sorted(s))[::-1]
    
# line4 
# return ''.join(sorted(s, reverse=True))
# 도 가능
