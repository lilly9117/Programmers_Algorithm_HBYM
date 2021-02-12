def solution(n, m):
    answer = []
    # 최대공약수
    for i in range(1,n+1):
        if n % i == 0:
            if m % i == 0:
                answer1 = i
    
    if i == 1:
        answer2 = n*m
    else:
        answer2 = answer1 * ( n // answer1) * (m //answer1)
    answer = [answer1, answer2]
    return answer

