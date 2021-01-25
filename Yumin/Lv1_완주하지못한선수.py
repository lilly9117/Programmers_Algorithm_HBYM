#https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    ans = list((collections.Counter(participant)-collections.Counter(completion)).keys())[0]
    return ans

#ans -> list((~).keys())[0]에서 list 빼먹는 바람에 시간 오지게 걸렸음,, 현타온다