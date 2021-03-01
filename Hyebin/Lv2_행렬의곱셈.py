def solution(arr1, arr2):

    one_len = len(arr1) #3
    two_len = len(arr1[0]) #2
    three_len = len(arr2[0]) #2

    answer = [[0 for _ in range(three_len)] for _ in range(one_len)]

    for i in range(one_len):
        for j in range(two_len):
            for k in range(three_len):
                answer[i][k] += (arr1[i][j] * arr2[j][k])
        
    return answer

# arr1 = [[1, 4], [3, 2], [4, 1]]
# arr2 = [[3,3],[3,3]]
# print(solution(arr1, arr2))