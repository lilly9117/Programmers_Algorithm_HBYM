def solution(s):
    # answer = True
    q = []
    for i in range((len(s))):
        if s[i] == '(':
            q.append('(')
        else:
            try: q.pop()
            except: 
                return False
    if len(q) == 0:
        return True
    return False

