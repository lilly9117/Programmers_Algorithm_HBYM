def solution(s):
    answer = []
    s= s.split(' ')
    for word in s:
        tmp=''
        for j in range(len(word)):
            tmp+= word[j].upper() if j%2==0 else word[j].lower()
        answer.append(tmp)
    return ' '.join(answer)


# failed solution (ㅠㅠ)
# def solution(s):
#     answer = []
#     s = ' '.join(s.split())
#
#     for i in range(len(s)):
#         if s[i] == ' ':
#             tmp = ' '
#         elif i % 2 == 0:
#             tmp = s[i].upper()
#         else:
#             tmp = s[i].lower()
#         answer.append(tmp)
#
#     return ''.join(answer)