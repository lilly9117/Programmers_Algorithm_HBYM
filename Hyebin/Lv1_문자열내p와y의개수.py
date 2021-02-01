import collections

def solution(s):
    answer = True
    
    s = s.lower()
    result = collections.Counter(s)
    key = list(result.keys())

    if 'p' in key or 'y' in key:
        if result['p'] != result['y']:
            answer = False
    return answer
