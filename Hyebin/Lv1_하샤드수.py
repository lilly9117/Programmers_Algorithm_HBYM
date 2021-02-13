def solution(x):
    answer = True
    xsum = sum([int(i) for i in str(x)])
    if x % xsum == 0:
        answer = True
    else:
        answer = False
    return answer

#sol
#return n % sum([int(c) for c in str(n)]) == 0