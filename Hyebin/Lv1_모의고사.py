def solution(answers):
    answer = []

    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    student = [one, two, three]

    count_yes = [0,0,0]

    for i in range(3):
        for j in range(len(answers)):
            if student[i][j % len(student[i])] == answers[j]:
                count_yes[i] += 1

    for i in range(3):
        if count_yes[i] == max(count_yes):
            answer.append(i+1)
            
    answer.sort()
    return answer


# answers = [1,3,2,4,2]
# print(solution(answers))