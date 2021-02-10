def solution(n):
    
    s_list = list(str(n))
    s_list.sort(reverse=True)
    answer = int(''.join(s_list))

    return answer
