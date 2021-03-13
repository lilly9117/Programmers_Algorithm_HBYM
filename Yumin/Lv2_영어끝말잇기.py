def solution(n, words):
    spoken = [words[0]]

    for w in range(1, len(words)):

        # 단어중복 or 끝말잇기 규칙 어긴 경우
        if words[w] in spoken or words[w - 1][-1] != words[w][0]:
            return [w % n + 1, w // n + 1]
        else:
            spoken.append(words[w])

    return [0, 0]