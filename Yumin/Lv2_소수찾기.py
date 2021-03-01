from itertools import permutations

def solution(numbers):
    answer = []

    # 가능한 모든 숫자 조합에 대해
    for i in range(1, len(numbers) + 1):
        for j in permutations(list(numbers), i):
            j = int(''.join(j))

            # 소수 판별
            for k in range(2, j):
                if j % k == 0:
                    break

            # 소수인 경우
            else:
                if j != 0 and j != 1:
                    answer.append(j)

    return len(set(answer))  # 중복되는 소수 제거