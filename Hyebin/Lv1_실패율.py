def solution(N, stages):
    s_rate = {}

    stage_len = len(stages)

    for s in range(1,N+1):
        if stage_len != 0:
            count = stages.count(s)
            s_rate[s] = count / stage_len
            stage_len -= count
        else:
            s_rate[s] = 0
    
    answer = sorted(s_rate, key = lambda x : s_rate[x], reverse = True)

    return answer

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# print(solution(N,stages))          
