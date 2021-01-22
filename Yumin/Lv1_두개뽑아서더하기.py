# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(n):
    ans = set()
    for i in list(combinations(n, 2)):
        ans.add(sum(i))
    return sorted(ans)