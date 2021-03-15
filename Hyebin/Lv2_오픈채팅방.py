def solution(record):
    answer = []
    user_dict = {}

    for r in record:
        if (r.split(' ')[0] == 'Enter') | (r.split(' ')[0] == 'Change'):
            user_dict[r.split(' ')[1]] = r.split(' ')[2]
    
    for r in record:
        if r.split(' ')[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user_dict[r.split(' ')[1]]))
        elif r.split(' ')[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(user_dict[r.split(' ')[1]]))
        else: pass
    
    return answer

# record = ["Ent(er uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))
