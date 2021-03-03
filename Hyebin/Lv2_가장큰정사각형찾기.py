def solution(board):
    h = len(board)
    w = len(board[0])

    for i in range(1,h):
        for j in range(1,w):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], min(board[i-1][j], board[i][j-1])) + 1
            # print(board)
    answer = max([num for row in board for num in row]) **2
    return answer

# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	
# print(solution(board))