import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    a = heapq.heappop(scoville)
    for i in range(1, len(scoville)):
        b = heapq.heappop(scoville)
        a = heapq.heappush(scoville, a + b*2)
        a = heapq.heappop(scoville)
        if a >= K: return i
    return -1 #impossible


# fail - min 연산 효율 very low
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#
#     while True:
#         if len(scoville) <2:
#             answer=-1
#             break
#         elif min(scoville) > K:
#             break
#         else:
#             a= scoville[0] + scoville[1]*2
#             scoville[0]=a
#             del scoville[1]
#             answer+=1
#     return answer