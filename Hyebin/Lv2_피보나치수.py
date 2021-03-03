def solution(n):
    fibo_list = []
    for i in range(n):
        if i < 2:
            fibo_list.append(1)
        else:
            fibo_list.append(fibo_list[i-2] + fibo_list[i-1])
    answer = fibo_list[-1] % 1234567

    return answer
