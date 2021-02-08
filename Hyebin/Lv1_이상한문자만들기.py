def solution1(s): # time over
    answer = []
    s_list = s.split()

    for i in s_list:
        new_i = ''
        for j in range(len(i)):
            if j % 2 == 0:
                new_i += i[j].upper()
            else:
                new_i += i[j].lower()
        answer.append(new_i)

    answer = ' '.join(answer)

    return answer

def solution(s):
    answer = ''
    s_list = s.split(' ')
    for i in s_list:
        for index, w in enumerate(i):
            answer += w.upper() if index % 2 == 0 else w.lower()
        
        answer += ' '
    
    answer = answer[:-1]
    return answer 
