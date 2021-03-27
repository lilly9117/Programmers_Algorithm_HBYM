"sol: https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS"


def solution(numbers, target):

    answer = 0

    queue = [[numbers[0],0],[-1*numbers[0],0]]

    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx +=1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer +=1

    return answer


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))