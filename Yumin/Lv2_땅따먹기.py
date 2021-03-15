#https://eda-ai-lab.tistory.com/480

def solution(land):

    for i in range(0,len(land)-1):
        land[i+1][0]+= max(land[i][1], land[i][2], land[i][3])
        land[i+1][1]+= max(land[i][0], land[i][2], land[i][3])
        land[i+1][2]+= max(land[i][0], land[i][1], land[i][3])
        land[i+1][3]+= max(land[i][0], land[i][1], land[i][2])

    return max(land[len(land)-1])

# fail
# def solution(land):
#     answer = 0
#     cant = 0
#
#     a = []
#     for i in land[0]:
#         cant = land[0].index(i)
#         answer += i
#         for j in range(1, len(land)):
#
#             # max 겹치지 않을 때
#             tmp = max(land[j])
#             if land[j].index(tmp) != cant:
#                 answer += tmp
#                 cant = land[j].index(tmp)
#
#             # max 겹칠 때
#             else:
#                 land[j][land[j].index(tmp)] = 0
#                 tmp = max(land[j])
#                 answer += tmp
#                 cant = land[j].index(tmp)
#         a.append(answer)
#         answer = 0
#     return max(a)