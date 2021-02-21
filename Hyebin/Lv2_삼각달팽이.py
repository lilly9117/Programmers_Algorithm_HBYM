from itertools import chain

def solution(n):
    answer = []
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y, x = -1, 0
    number = 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            maps[y][x] = number
            number +=1
            # print(x)
            # print(y)
            # print('-------------')
    answer = [i for i in chain(*maps) if i != 0]
    return answer

# n=4
# print(solution(n))
# n=5
# print(solution(n))
# n=6
# print(solution(n))