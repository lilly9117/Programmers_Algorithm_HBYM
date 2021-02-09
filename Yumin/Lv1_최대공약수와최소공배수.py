#https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []

    # 최대공약수
    i = min(n, m)
    while i >= 0:
        if n % i == 0 and m % i == 0 or i == 1:
            answer.append(i)
            break
        else:
            i -= 1

    # 최소공배수
    answer.append(n * m / answer[0])

    return answer

#a*b=둘의 최대공약수*최소공배수