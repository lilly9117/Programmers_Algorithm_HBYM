def solution(s):
    split_s = s.split(' ')
    answer = ''

    for i in split_s:
        cap_i = i.capitalize()
        if answer == '':
            answer = cap_i
        else:
            answer+= ' ' + cap_i
    return answer

# s = "3people unFollowed me"
# print(solution(s))

#sol
# return s.title()
# 이렇게 간단한 함수가 있었다니,,,,,,,ㅠ