def solution(n, lost, reserve):
    answer = 0

    reser = set(reserve) - set(lost)
    los = set(lost) - set(reserve) #추가
    # print(reser)
    # print(los)
    # exit()
    for r in reser:
        if r-1 in los:
            los.remove(r-1)
        elif r+1 in los:
            los.remove(r+1)
    
    answer = n - len(los)
    
    return answer

# n = 5
# lost = [2,4]
# reserve = [3]
# print(solution(n,lost,reserve))