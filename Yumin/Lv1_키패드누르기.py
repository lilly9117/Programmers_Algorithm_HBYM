https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    l, r = [4, 1], [4, 3]  # 초기 손가락 위치

    # 키패드
    keys = [[4, 2],
            [1, 1], [1, 2], [1, 3],
            [2, 1], [2, 2], [2, 3],
            [3, 1], [3, 2], [3, 3]]

    for n in numbers:
        # 왼쪽 열
        if n in [1, 4, 7]:
            tmp = 'L'
            l = keys[n]
        # 오른쪽 열
        elif n in [3, 6, 9]:
            tmp = 'R'
            r = keys[n]
        # 가운데 열
        else:
            # 왼 오 거리
            l_dist = abs(keys[n][0] - l[0]) + abs(keys[n][1] - l[1])
            r_dist = abs(keys[n][0] - r[0]) + abs(keys[n][1] - r[1])
            if l_dist != r_dist:  # 거리다를때
                if l_dist < r_dist:
                    tmp = 'L'
                    l = keys[n]
                else:
                    tmp = 'R'
                    r = keys[n]
            else:  # 거리 동일
                tmp = hand[0].upper()
                if tmp == 'L':
                    l = keys[n]
                else:
                    r = keys[n]
        answer += tmp
        print(l, r, n, keys[n], tmp)

    return answer