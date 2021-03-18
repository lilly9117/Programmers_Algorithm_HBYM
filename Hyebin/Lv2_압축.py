# -*- coding: utf-8 -*- 
# 다시 공부,,,
# LZW 알고리즘

def solution(msg):
    a_dic = {chr(i): i+1-ord('A') for i in range(ord('A'), ord('Z')+1)}
    answer = []
    start, end = 0, 0 

    while end < len(msg):
        if msg[start:end+1] in a_dic:
            end +=1
        else:
            a_dic[msg[start:end+1]] = len(a_dic) +1
            answer.append(a_dic[msg[start:end]])
            start, end = end, end
    
    answer.append(a_dic[msg[start:end+1]])
    return answer

    
msg = 'KAKAO'
print(solution(msg))
msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))


