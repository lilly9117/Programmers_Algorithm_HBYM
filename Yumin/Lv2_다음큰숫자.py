def solution(n):
    zero = bin(n).count('1')

    i = n + 1
    while True:
        if zero == bin(i).count('1'):
            return i
        i += 1