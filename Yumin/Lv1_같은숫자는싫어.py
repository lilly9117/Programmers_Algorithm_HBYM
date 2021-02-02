#https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i==0:
            answer.append(arr[i])
        elif arr[i-1]==arr[i]:
            pass
        else:
            answer.append(arr[i])

    return answer
