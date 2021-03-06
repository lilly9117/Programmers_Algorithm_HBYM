def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse= True)
    
    l = [a*b for a,b in zip(A,B)]
    answer = sum(l)

    return answer

# A = [1,4,2]
# B = [5,4,4]
# print(solution(A,B))