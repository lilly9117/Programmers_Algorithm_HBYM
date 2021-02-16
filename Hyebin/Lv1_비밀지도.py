def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        # print(bin(a1))
        # print(bin(a2))
        # print(bin(a1 | a2))
        ans_num = str(bin(a1 | a2)[2:])
        if len(ans_num) < n:
            ans_num = '0'*(n-len(ans_num))+ ans_num
        ans_num = ans_num.replace('1', '#')
        ans_num = ans_num.replace('0', ' ')
        answer.append(ans_num)
    return answer

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# print(solution(n,arr1, arr2))