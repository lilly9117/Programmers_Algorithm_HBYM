def solution(name):
    answer = 0
    spell = [ord(i) - ord('A') for i in name]

    i = 0
    while True:
        answer += 26 - spell[i] if spell[i] > 13 else spell[i]
        spell[i] = 0

        # 이름만들기가 끝나면 break
        if sum(spell) == 0:
            break

        # 좌/우 방향 중 0(=A)을 먼저 만나는 방향으로 이동
        left, right = 0, 0
        while spell[i - left] == 0:
            left += 1
        while spell[i + right] == 0:
            right += 1

        answer += left if left < right else right
        i += -left if left < right else right

    return answer


# fail - ABAAAAAAABA 
# def solution(name):
#     answer = len(name) - 1
#     spell = [ord(i) - 65 for i in name]
#
#     for s in spell:
#         answer += 26 - s if s > 13 else s
#
#     if spell[1] == 0:
#         answer -= 1
#
#     return answer
# A-0 ~ Z-25