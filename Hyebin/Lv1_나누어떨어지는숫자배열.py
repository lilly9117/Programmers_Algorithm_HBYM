def solution(arr, divisor):
    answer = []
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    if not answer:
        answer.append(-1)
    answer.sort()
    return answer


# def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]