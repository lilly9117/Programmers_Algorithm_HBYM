def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = list(skill)

    for tree in skill_trees:
        step_tree = []

        for s in list(tree):
            if s in skill:
                step_tree.append(s)
                
        for index, s_t in enumerate(step_tree):
            if s_t != skill[index]:
                answer -=1
                break
    return answer

# skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# print(solution(skill, skill_trees))