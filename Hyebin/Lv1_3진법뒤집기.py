def solution(n):
    answer= 0
    temp = ''
    while n:
        temp += str(n % 3)
        n = int(n/3)
    # print(temp)
    for i in range(len(temp)):
        answer += int(temp[-(i+1)]) * 3**i
    return answer
