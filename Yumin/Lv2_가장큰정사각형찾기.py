#https://velog.io/@djagmlrhks3/Algorithm-Programmers-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-by-Python

def solution(board):
    answer = 1234

    for b in board:
        if sum(b)>0:
            answer=1
            break
    else:
        return 0  #모든 원소가 0

    # 2*2 로 탐색
    for x in range(1, len(board)):
        for y in range(1, len(board[0])):
            # 4개의 숫자가 모두 1 이상인 경우
            if board[x-1][y-1]>0 and board[x-1][y]>0 and board[x][y-1]>0 and board[x][y]>0:
                # 우측 하단 값& answer 업데이트
                board[x][y]= min(board[x-1][y-1], board[x][y-1], board[x-1][y]) + 1
                answer= max(answer, board[x][y])

    return answer**2