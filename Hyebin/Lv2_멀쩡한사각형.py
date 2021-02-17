import math

def solution(w,h):
    err = w+h - math.gcd(w,h)
    answer = w*h - err
    return answer

# w = 8
# h= 12
# print(solution(w,h))

