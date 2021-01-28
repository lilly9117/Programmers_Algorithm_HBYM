#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    ans=[]
    for n in range(len(commands)):
        i,j,k = commands[n][0], commands[n][1], commands[n][2]
        ans.append(sorted(array[i-1:j])[k-1])
    return ans