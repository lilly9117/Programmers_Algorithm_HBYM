def solution(n):
    answer = 0

    two_n_count = bin(n).count('1')
    for i in range(n+1, 10000001):
        if bin(i).count('1') == two_n_count:
            answer = i 
            break
    return answer
