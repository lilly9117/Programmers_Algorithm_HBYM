def solution(s):
    q = []

    for i in range(len(s)):
        # print(i)
        if len(q) == 0:
            q.append(s[i])
        elif q[-1] == s[i]:
            q.pop(-1)
        else:
            q.append(s[i])
        # print(q)
    if len(q) == 0:
        return 1
    else:
        return 0 

# s = 'baabaa'
# print(solution(s))
