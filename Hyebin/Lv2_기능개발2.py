#sol : https://programmers.co.kr/learn/courses/30/lessons/42586/solution_groups?language=python3

def solution(progresses, speeds):
    queue=[]
    for p, s in zip(progresses, speeds):
        if len(queue)==0 or queue[-1][0] < -((p-100)//s):
            queue.append([-((p-100)//s),1])
        else:
            queue[-1][1]+=1
        # print(queue)
    return [q[1] for q in queue]

# progresses = [93, 30, 55]
# speeds = [1,30,5]
# print(solution(progresses, speeds))

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]	
# print(solution(progresses, speeds))