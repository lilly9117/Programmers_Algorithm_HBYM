# sol : https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    # print(dart) 
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# dartResult = '1S2D*3T'
# print(solution(dartResult))