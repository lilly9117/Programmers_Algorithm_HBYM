def solution(n):
    answer = 0
    s_list = list(str(n))
    n_list = list(map(int, s_list))

    answer = sum(n_list)

    return answer
