def solution(strings, n):
    answer = []
    n_s = []
    
    strings.sort()

    for s in strings:
        n_s.append(s[n])
    
    n_s.sort()

    for s in n_s:
        for st in strings:
            if st[n] == s and st not in answer:
                answer.append(st)
    return answer

