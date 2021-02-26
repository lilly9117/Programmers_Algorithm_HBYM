def solution(priorities, location):
    answer = 0
    m = max(priorities)

    while True:
        m = max(priorities)
        c = priorities.pop(0)

        # 현재문서-> 인쇄
        if c == m:
            answer += 1
            if location == 0:
                break  # 요청문서 인쇄 후 break
            else:
                location -= 1

        # 현재문서 -> 대기목록 마지막으로
        else:
            priorities.append(c)
            location = location - 1 if location != 0 else len(priorities) - 1

    return answer


# fail
# def solution(priorities, location):
#     answer = 0
#     want = priorities[location]
#
#     while want in priorities:
#         if len(priorities) < 2:
#             break
#         elif max(priorities) > priorities[0]:
#             priorities.append(priorities[0])
#             del priorities[0]
#             answer += 1
#             want = priorities[location - 1]
#     return answer
