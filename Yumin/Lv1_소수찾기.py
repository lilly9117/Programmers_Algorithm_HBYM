# https://ychae-leah.tistory.com/190

def solution(n):
    sieve = [0] * (n+1)

    m = int(n ** 1/2)
    for i in range(2, m + 1): #n의 최대 약수는 under sqrt(n) (by 에라토스테네스의 체)
        if sieve[i] == 0: #i가 소수
            for j in range(2*i, n+1, i): #i이후 i의 배수를 1로
                sieve[j] = 1

    return sieve[2:].count(0)  #0,1을 제외한 소수 개수


# fail (time out)
# def solution(n):
#     answer = 0
#     tmp = 0
#
#     for i in range(1, n + 1):
#         tmp = 0
#         for j in range(2, i - 1):
#             if i % j == 0:
#                 tmp = 1
#                 break
#         if tmp != 1 and i != 1:
#             answer += 1
#             print(i)
#
#     return answer