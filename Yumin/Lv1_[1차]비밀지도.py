def solution(n, arr1, arr2):
    answer = []
    b1, b2 = [], []

    # 진수변환
    for i in range(n):
        b1.append(format(arr1[i], 'b').zfill(n))
        b2.append(format(arr2[i], 'b').zfill(n))

    # '#' or ' '
    for i in range(n):
        tmp = []
        for j in range(n):
            t = ' ' if b1[i][j] == '0' and b2[i][j] == '0' else '#'
            tmp.append(t)
        answer.append(''.join(tmp))

    return answer