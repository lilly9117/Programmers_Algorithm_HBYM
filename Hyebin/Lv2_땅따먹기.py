def solution(land):
    answer = 0

    for i in range(1, len(land)): #3
        for j in range(len(land[0])):
            # print(land[i-1][:j])
            # print(land[i-1][j+1:])
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:]) # 가장 큰수 더해가는 형태
            # print(land[i-1][:j] + land[i-1][j+1:])
            # print(land)
            # print('**')

    # print(land)
    
    answer = max(land[-1]) # 
    
    return answer

# land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
# print(solution(land))
