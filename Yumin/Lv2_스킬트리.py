def solution(skill, skill_trees): 
    answer = 0

    for st in skill_trees:
        temp = {}

        # skill 포함여부& index
        for i, s in enumerate(skill):
            if st.find(s) != -1: #해당 skill_trees에 skill이 미포함인 경우 count X
                temp[s] = st.find(s) # 스킬명& index 저장
        # print(list(temp.values()), sorted(list(temp.values())), ''.join(temp.keys()), skill[:len(temp)])

        # 1) temp의 value 순서가 skill의 순서와 같고(temp value 오름차순)
        # 2) 동시에 temp와 skill이 가진 값과 순서가 동일한 경우 answer+=1
        if list(temp.values()) == sorted(list(temp.values())) and ''.join(temp.keys()) == skill[:len(temp)]:
            answer += 1
    return answer

# skill이 "CBD", skill_trees가 ["BACDE", "CBADF", "AECB", "BDA"] 일 때,
# print(list(temp.values()), sorted(list(temp.values())), ''.join(temp.keys()), skill[:len(temp)])
# [2, 0, 3] [0, 2, 3] CBD CBD
# [0, 1, 3] [0, 1, 3] CBD CBD
# [2, 3] [2, 3] CB CB
# [0, 1] [0, 1] BD CB
