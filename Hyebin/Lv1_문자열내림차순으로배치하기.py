def solution(s):
    answer = ''
    up = []
    down = []
    for i in s:
        if i.isupper:
            up.append(i)
        else:
            down.append(i)
    up.sort(reverse = True)
    down.sort(reverse = True)
    answer = ''.join(down+up)
    return answer
