def solution(n):
    answer = ''
    num = [1, 2, 4]

    while n > 0:
        temp = num[(n - 1) % 3]
        answer += str(temp)
        n = (n - 1) // 3

    return answer[::-1]


# 1,2,4 반복 -> n-1이 십의자리 결정

# 3**1: 1 2 4
# 3**2: 11 12 14 21 22 24 41 42 44
# 3**3: 111