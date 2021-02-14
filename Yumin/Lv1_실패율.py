def solution(N, stages):

    answer = {}
    trial = len(stages) #도전자 수

    for i in range(1, N + 1):
        if trial != 0:
            cnt = stages.count(i) #실패자 수
            answer[i] = cnt / trial #실패율
            trial -= cnt #실패자는 next stage X
        else:
            answer[i] = 0 #도전자 0명 -> 실패율 0

    return sorted(answer, key=lambda x: 1 - answer[x])
    # 원래 lambda x : answer[x] 을 사용하려 하였으나, stage 123의 실패율이 같을 때 reverse시 321이므로 X
    # 따라서 reverse 사용X, 1-실패율 기준으로 sorting