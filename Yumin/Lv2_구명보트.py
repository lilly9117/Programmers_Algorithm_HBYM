def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1

    while b - a > 0:
        # 남은 사람의 몸무게가 limit/2 이하 > 남은 사람 수의 절반만큼 구명보트 필요
        if people[b] <= limit / 2:
            answer += (b - a + 1) // 2 + (b - a + 1) % 2
            break

        # 남은 사람 중 가장 가벼운+무거운<limit 여부 확인
        if people[a] + people[b] <= limit:
            a += 1
            b -= 1
        else:
            b -= 1
        answer += 1

        if a == b:
            answer += 1

    return answer

# fail - 시간초과
# pop(0) 연산의 시간복잡도: O(n)
# def solution(people, limit):
#     answer= 0
#     people.sort()

#     while len(people)>0:
#         if people[-1] <= limit/2:
#             answer+= len(people)//2 + len(people)%2
#             break

#         if len(people)>1 and people[0]+people[-1] <= limit:
#             people.pop()
#             people.pop(0)
#         else:
#             people.pop()
#         answer+=1

#     return answer