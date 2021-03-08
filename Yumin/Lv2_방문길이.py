def solution(dirs):
    # UDRL
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    now_x, now_y = 0, 0
    visit = []

    for d in dirs:
        next_x = now_x + move[d][0]
        next_y = now_y + move[d][1]

        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            visit.append((now_x, now_y, next_x, next_y))  # 출발>도착
            visit.append((next_x, next_y, now_x, now_y))  # 도착>출발
            now_x, now_y = next_x, next_y

    return len(set(visit)) // 2  # 겹치는 길 경로 제거 후 걸어본 길의 길이 return 