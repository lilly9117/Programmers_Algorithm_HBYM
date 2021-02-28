def solution(people, limit):
    answer = 0
    people.sort()
    # 80 70 50 50 
    i = 0
    j = len(people) - 1
    while i <= j:
        print(i,j)
        answer +=1
        if people[i] + people[j] <= limit:
            i +=1
        j -=1
        
    return answer

# people = [70, 50, 80, 50]
# limit = 100
# print(solution(people, limit))
