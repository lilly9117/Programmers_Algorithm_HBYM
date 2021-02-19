def solution(progresses, speeds):
    answer = []
    count = 0
    curr_day = 0
    while len(progresses) > 0:
        if (progresses[0] + speeds[0]*curr_day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count +=1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            curr_day +=1
    answer.append(count)

    return answer

# progresses = [93, 30, 55]
# speeds = [1,30,5]
# print(solution(progresses, speeds))

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]	
# print(solution(progresses, speeds))
