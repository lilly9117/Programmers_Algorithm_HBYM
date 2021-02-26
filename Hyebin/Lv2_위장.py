from collections import Counter
#from funtools import reduce 사용가능...

def solution(clothes):
    answer = 1
    type_count = Counter([type for _,type in clothes])
    # print(type_count)

    for key in type_count:
        answer *= (type_count[key]+1)
    answer-=1
    return answer

# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# print(solution(clothes))