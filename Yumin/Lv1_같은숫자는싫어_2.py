#https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    for a in arr:
        if len(answer)==0 or a!=answer[-1]:
            answer.append(a)

    return answer
