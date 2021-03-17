import re
from collections import Counter 

def solution(str1, str2):
    answer = 0

    str1, str2 = str1.lower(), str2.lower()

    two_s = re.compile('[a-z][a-z]')

    str1_t = two_s.findall(" ".join(str1[i:i+2] for i in range(0, len(str1))))
    str2_t = two_s.findall(" ".join(str2[i:i+2] for i in range(0, len(str2))))

    if len(str1_t) == len(str2_t) == 0:
        return 65536

    count_str1, count_str2 = Counter(str1_t), Counter(str2_t)

    intersect = set(str1_t) & set(str2_t)
    union = set(str1_t) | set(str2_t)

    up_intersect = sum([min(count_str1[i], count_str2[i]) for i in intersect ])
    down_union = sum([max(count_str1[i], count_str2[i]) for i in union])

    jac = up_intersect / down_union
    answer = int(jac * 65536)
    return answer

str1 = 'FRANCE'
str2 = 'french'
print(solution(str1,str2))