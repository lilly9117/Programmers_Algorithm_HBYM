#https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''

    # 3진법 변환 & 뒤집기
    while n > 0:
        n, m = divmod(n, 3)
        answer += str(m)

    return int(answer, 3)  # 10진법

# answer= str(answer)[::-1]
# 문자열 뒤집을 때 사용하려 했으나 필요X