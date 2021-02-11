def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
        return answer
    else:
        arr.remove(min(arr))
        return arr


# arr = [4,3,2,1]
# print(solution(arr))

# arr = [10]
# print(solution(arr))