#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    res = set(reserve) - set(lost)  # 여벌 have
    los = set(lost) - set(reserve)  # 체육복 없음

    for r in res:
        if r - 1 in los:
            los.remove(r - 1)
        elif r + 1 in los:
            los.remove(r + 1)
    return n - len(los)

# 학생 r에게 여벌 체육복이 있을 때,
# (r-1, (r+1)번째 학생이 체육복이 없으면 빌려주고 remove

# same with line 2,3
#    res = [r for r in reserve if r not in lost]
#    los = [l for l in lost if l not in reserve]