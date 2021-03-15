from collections import Counter

def solution(s):
    answer = []
    
    d_s = s.replace('{','').replace('}','').split(',')

    most_c = Counter(d_s).most_common()

    for d in most_c:
        answer.append(int(d[0]))
    return answer

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# print(solution(s))

'''
solution**
import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

'''

