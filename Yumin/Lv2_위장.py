from collections import Counter

def solution(clothes):
    cnt = Counter([j for i, j in clothes])

    answer = 1
    for j in cnt:
        answer *= cnt[j] + 1

    return answer - 1

# 각 의상종류+1 한 값을 모두 곱한 후 -1(의상이 0인 경우)