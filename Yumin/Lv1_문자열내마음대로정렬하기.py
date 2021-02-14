def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])

# 풀어쓰면
# def solution(strings, n):
#     answer= sorted(strings)
#     answer= sorted(answer, key=lambda x:x[n])
#     return answer