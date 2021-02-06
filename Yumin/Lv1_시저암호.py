#https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    s = list(s)
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(len(s)):
        if s[i] in big:
            s[i] = big[(big.index(s[i]) + n) % 26]
        elif s[i] in small:
            s[i] = small[(small.index(s[i]) + n) % 26]
        else:
            pass
    return ''.join(s)