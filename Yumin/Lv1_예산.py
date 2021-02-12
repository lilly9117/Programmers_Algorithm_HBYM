def solution(d, budget):
    answer = 0
    d = sorted(d)

    cnt = 0
    while cnt < len(d):
        budget -= d[cnt]
        if budget < 0:
            break
        else:
            answer += 1
            cnt += 1

    return answer