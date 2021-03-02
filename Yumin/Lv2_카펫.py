def solution(brown, yellow):
    tot = brown + yellow
    a = 1
    while True:
        b = tot / a
        if (a - 2) * (b - 2) == yellow and a * b == tot:
            return [b, a]
        a += 1

# 갈색 사각형 크기  :  a*b
# 노란색 사각형 크기 : (a-2)*(b-2)