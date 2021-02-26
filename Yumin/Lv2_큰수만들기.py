def solution(number, k):
    answer = []

    # 들어오는 값 > answer[-1]이면 기존 값을 제거 후 새로운 값으로
    for n in number:
        while k > 0 and len(answer) > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)

    # 남은 k만큼 제거
    if k != 0:
        answer = answer[:-k]

    return ''.join(answer)



# failed - 자리바꾸기 불가능
# def solution(number, k):
#     answer = ''
#     number= list(map(int,number))
#
#     while k>0:
#         a= min(number)
#         for i in number:
#             if i==a and k!=0:
#                 number.remove(i)
#                 k-=1
#             if k==0:
#                 break
#     return ''.join(str(number))