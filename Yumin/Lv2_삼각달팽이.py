def solution(n):
    answer = []
    board = [[0] * n for _ in range(n)]

    # 가능한 방향 -> 우, 하, 대각선 왼쪽 위
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    num = n * (n + 1) // 2  # 필요한 숫자 수
    x, y = 0, 0
    d = 0  # 방향
    cnt = 1

    while num >= cnt:
        # board에 숫자 할당
        if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
            board[x][y] = cnt
            cnt += 1

        # 원래 칸으로 돌아와서 + 방향 조정
        else:
            x -= dx[d]
            y -= dy[d]
            d = (d + 1) % 3

        # x,y 좌표 이동
        x += dx[d]
        y += dy[d]

    for x in range(n):
        for y in range(x + 1):
            answer.append(board[x][y])

    return answer
