def solution(n):
    answer = []
    s_list = list(str(n))
    answer = list(map(int, s_list))
    answer.reverse()

    return answer
