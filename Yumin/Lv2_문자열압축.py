def solution(s):
    answer = [len(s)]  # 압축 전 문자열 길이

    for cut in range(1, len(s) // 2 + 1):
        tmp = ''
        cnt = 1
        a = s[:cut]

        for i in range(cut, cut + len(s), cut):

            # 직전 단위와 동일한 경우
            if a == s[i:i + cut]:
                cnt += 1

            # 직전 단위와 다른 경우 - 문자열 압축
            else:
                tmp += a if cnt == 1 else str(cnt) + a
                a = s[i:i + cut]
                cnt = 1

        answer.append(len(tmp))  # cut단위로 압축한 문자열 길이
    return min(answer)