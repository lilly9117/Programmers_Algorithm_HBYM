def solution(s):

    stack=[s[0]]
    for i in range(1,len(s)):
        if len(stack)>0 and stack[-1]==s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return 0 if len(stack)!=0 else 1


# fail - 시간초과
# def solution(s):
#     s = list(s)
#     new_s = s
#
#     while True:
#         for i in range(1, len(s)):
#             if s[i - 1] == s[i]:
#                 del new_s[i - 1]
#                 del new_s[i - 1]
#                 break
#         else:
#             s = new_s
#             break
#         s = new_s
#
#     return 0 if len(s) != 0 else 1