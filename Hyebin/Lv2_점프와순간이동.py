def solution(n):
    ans = 0
    
    while n > 0:
        q, r = divmod(n,2)
        n = q
        if r != 0:
            ans +=1
    return ans

#sol
    # return bin(n).count('1')

# N = 5
# print(solution(N))
# N = 6
# print(solution(N))
# N = 5000
# print(solution(N))