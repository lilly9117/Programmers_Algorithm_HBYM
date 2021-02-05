def solution(array, commands):
    answer = []
    for com in commands:
        new_list = array[com[0]-1:com[1]]
        new_list.sort()
        answer.append(new_list[com[2]-1])
    return answer

# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))