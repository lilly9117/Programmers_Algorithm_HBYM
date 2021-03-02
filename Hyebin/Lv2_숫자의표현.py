def solution(n):
    answer = 0

    for i in range(1,n//2+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer +=1
                break
            elif temp > n:
                break
            else:
                continue

    answer +=1 
    return answer

