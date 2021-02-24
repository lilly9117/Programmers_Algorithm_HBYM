from itertools import permutations 

def solution(numbers):
    answer = 0
    num_l = list(numbers)

    for i in range(2, len(numbers)+1):
        num_p = list(permutations(numbers, i))
        for j in num_p:
            if len(j) <= len(numbers):
                num_l.append(''.join(j))
    new_l = list(set([int(x) for x in num_l]))


    if new_l.count(1):
        new_l.remove(1)
    if new_l.count(0):
        new_l.remove(0)
    # print(new_l)

    for n in new_l:
        i = 2
        while i * i <= n:
            if n % i == 0:
                answer -=1
                break
            i +=1
        answer +=1

    return answer

# numbers = "17"
# print(solution(numbers))
# numbers = "011"
# print(solution(numbers))

