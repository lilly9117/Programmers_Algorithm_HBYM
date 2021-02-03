def solution(n):
    answer = 0

    numbers = set(range(2,n+1))

    for i in range(2,n+1):
        if i in numbers:
            # print(numbers)
            numbers -= set(range(2*i,n+1,i))
    answer = len(numbers)

    return answer
