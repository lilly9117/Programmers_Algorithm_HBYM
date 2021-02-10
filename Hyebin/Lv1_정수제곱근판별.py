import math

def solution(n):
    answer = 0
    sqrt_n = math.sqrt(n)
    if sqrt_n == int(sqrt_n):
        answer = int(pow(sqrt_n+1,2))
    else:
        answer = -1
    return answer