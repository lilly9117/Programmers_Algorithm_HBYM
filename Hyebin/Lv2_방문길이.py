# -*- coding: utf-8 -*- 

def solution(dirs):
    answer = 0

    cur_x, cur_y = (0,0)
    
    directions = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    
    visit = set() #집합으로 설정해서 겹치는 길 없게 
    for d in dirs:
        next_x, next_y = cur_x + directions[d][0], cur_y + directions[d][1]

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            visit.add((cur_x, cur_y, next_x, next_y))
            visit.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    # print(visit)
    answer = len(visit) // 2

    return answer

# dirs = "ULURRDLLU"
# print(solution(dirs))
# dirs = "LULLLLLLU"
# print(solution(dirs))

