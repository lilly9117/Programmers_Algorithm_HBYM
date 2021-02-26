def solution(progresses, speeds):
    answer = []
    day = []

    # 기능별 완료까지 걸리는 일수
    for i in range(len(progresses)):
        temp = (99 - progresses[i]) // speeds[i] + 1
        day.append(temp)

    while len(day) > 0:
        cnt = 1
        a = day.pop(0)
        day2 = day.copy()
        for i in range(len(day)):
            if a >= day[i]:
                cnt += 1
                day2.pop(0)
            else:
                break
        answer.append(cnt)
        day = day2.copy()

    return answer
