from fractions import gcd

def solution(arr):
    answer = 1
    
    for i in arr:
        answer = answer * i / gcd(answer,i)
    return answer

# arr = [2,6,8,14]
# print(solution(arr))
