# 힙
# sol : https://somjang.tistory.com/entry/Programmers-%ED%9E%99-%EB%8D%94-%EB%A7%B5%EA%B2%8C-Python
import heapq

def solution(scoville, K):
    answer = -1
    count = 0

    check_flag = False
    heapq_scoville = heapq.heapify(scoville) #기존리스트 힙으로 변환

    while scoville[0] < K:
        min_first = heapq.heappop(scoville) #힙에서 원소삭제
        min_second = heapq.heappop(scoville)

        heapq.heappush(scoville, min_first + (min_second*2)) #힙에 원소추가

        if len(scoville) == 1 and scoville[0] < K:
            check_flag = True
            break

        count += 1

    if check_flag == False:
        answer = count

    return answer
