# https://itchallenger.tistory.com/86 

def solution(dartResult):
    answer = []
    point = {'S': 1, 'D': 2, 'T': 3}
    temp = ''

    for i, c in enumerate(dartResult):
        if c in point:
            answer.append(int(temp) ** point[c])  # 점수&SDT는 같이 있음
            temp = ''
        elif c == '*':
            answer[-1] = answer[-1] * 2
            if len(answer) >= 2:
                answer[-2] = answer[-2] * 2
        elif c == '#':
            answer[-1] = answer[-1] * -1
        else:
            temp += c
    return sum(answer)
