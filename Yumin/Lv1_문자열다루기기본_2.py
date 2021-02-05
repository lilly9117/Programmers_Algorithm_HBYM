#https://programmers.co.kr/learn/courses/30/lessons/12918

import re
def solution(s):    
    return len(s) in [4, 6] and s == ''.join(re.findall('\d+', s))
