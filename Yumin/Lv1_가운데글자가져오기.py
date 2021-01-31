#https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s) % 2 != 0:  # 홀수
        return s[(len(s) // 2)]
    else:  # 짝수
        return s[len(s) // 2 - 1:len(s) // 2 + 1]