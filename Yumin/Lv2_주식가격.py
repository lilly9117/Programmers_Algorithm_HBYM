def solution(prices): 
    answer = []

    for i, p in enumerate(prices):
        cnt = 0
        for j in range(i, len(prices)):
            if p > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt - 1)

    return answer
