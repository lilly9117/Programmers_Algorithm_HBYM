def solution(num):
    answer = 0

    # num=1 처리
    if num == 1:
        return answer

    while answer <= 500:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        answer += 1
        if num == 1:
            break
    return answer if answer < 500 else -1