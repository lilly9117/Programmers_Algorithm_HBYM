def solution(x, n):
    answer = []
    cnt, tmp = 0, x

    while cnt < n:
        answer.append(tmp)
        cnt += 1
        tmp += x

    return answer