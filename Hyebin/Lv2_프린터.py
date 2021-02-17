def solution(priorities, location):
    answer = 0
    m_p = max(priorities)

    while True:
        # print(m_p)
        c_p = priorities.pop(0)
        # print(c_p)
        if m_p == c_p:
            answer +=1
            if location == 0:
                break
            else:
                location -= 1
            m_p = max(priorities)
            # print('y')
        else:
            priorities.append(c_p)
            if location == 0:
                location = len(priorities) -1
            else:
                location -=1
        #     print('n')
        
        # print(priorities)
        # print(location)
            

    return answer

# priorities = [2,1,3,2]
# location = 2
# print(solution(priorities,location))