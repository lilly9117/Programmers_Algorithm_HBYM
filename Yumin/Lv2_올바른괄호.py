def solution(s):
    temp = []
    for i in s:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            else:
                del temp[-1]
    return True if len(temp) == 0 else False