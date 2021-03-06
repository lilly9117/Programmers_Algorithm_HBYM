def solution(arr):
    answer = []

    def dfs(x, y, n):
        # 타일 크기 1인 경우
        if n == 1:
            return [1, 0] if arr[y][x] else [0, 1]

        # 4등분하며 확인
        l_up = dfs(x, y, n // 2)
        l_down = dfs(x, y + n // 2, n // 2)
        r_up = dfs(x + n // 2, y, n // 2)
        r_down = dfs(x + n // 2, y + n // 2, n // 2)

        # 4개의 사각형의 수가 동일 - 압축
        # fail - 조건 l_up==l_down==r_up==r_down 로 부여했을 때
        if l_up == l_down == r_up == r_down == [0, 1] or l_up == l_down == r_up == r_down == [1, 0]:
            return l_up
        else:
            return list(map(sum, zip(l_up, l_down, r_up, r_down)))

    answer = dfs(0, 0, len(arr))

    return answer[::-1]