def solution(name):
    answer = 0
    name = list(name)

    loc_list = [min(ord(n)- ord('A'), ord('Z')-ord(n)+1) for n in name]
    curr = 0

    while True:
        # print(answer)
        answer += loc_list[curr]

        loc_list[curr] = 0
        if sum(loc_list) == 0:
            break
        
        left= 1
        right= 1

        while loc_list[curr - left] == 0:
            left +=1

        while loc_list[curr + right] == 0:
            right +=1
        # print(answer)
        if left < right:
            curr -= left
            answer += left
        else:
            curr += right
            answer += right

    return answer

# name = "JEROEN"
# print(solution(name))