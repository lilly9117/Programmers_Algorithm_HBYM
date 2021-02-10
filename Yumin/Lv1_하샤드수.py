def solution(x):
    #하샤드 수
    hsd= int(sum(map(int, str(x))))
    return True if x%hsd==0 else False