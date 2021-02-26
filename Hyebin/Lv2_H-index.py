def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # print(citations)
    # print(list(enumerate(citations, start=1)))
    new_list = list(map(min, enumerate(citations, start = 1))) # 어차피 h값으로 같고, 그중 최대값을 뽑으므로
    answer = max(new_list)
    return answer

# citations = [3, 0, 6, 1, 5]
# print(solution(citations))