#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    ans=[]
    for c in commands:
        i,j,k = c
        ans.append(sorted(array[i-1:j])[k-1])
    return ans