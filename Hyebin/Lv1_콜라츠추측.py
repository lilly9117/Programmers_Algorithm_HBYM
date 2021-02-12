def solution(num):
    answer = num
    count = 0
    while answer > 1:
        if answer % 2 == 0:
            answer = answer // 2
        else:
            answer = answer * 3 + 1
        count += 1
        if count >= 500:
            count = -1
            break
    return count

# n =6
# print(solution(n))
# n=16
# print(solution(n))
# n = 626331
# print(solution(n))