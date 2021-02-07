# solution
def solution(s, n):
    for i in range(len(s)):
        s = list(s)
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26 + ord('a'))
        answer = "".join(s)
    return answer

# s = "AB"
# n =1
# print(solution(s,n))
# s="z"
# n =1
# print(solution(s,n))
# s = "a B z"
# n = 4
# print(solution(s,n))