#hhttps://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    return arr if arr!=[] else [-1]