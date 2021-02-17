# 다시해보기,,,!!!!
# sol : https://covenant.tistory.com/169

def solution(dartResult):
    answer = 0
    i = 0
    temp = 0
    prev = -1
    dartResult = dartResult.replace('10','K')

    while i < len(dartResult):
        if dartResult[i].isdigit() or dartResult[i] == 'K':
            prev = temp
            answer += temp 
            if dartResult[i] == 'K':
                temp = 10
            else:
                temp = int(dartResult[i])
        elif dartResult[i] == 'S':
            temp *= 1
        elif dartResult[i] == 'D':
            temp = pow(temp,2)
        elif dartResult[i] == 'T':
            temp = pow(temp,3)
        elif dartResult[i] == '*':
            answer += prev
            temp *= 2
        elif dartResult[i] == '#':
            temp *= -1
        # print(temp)
        i +=1
    answer += temp
    return answer

dartResult = '1S2D*3T'
print(solution(dartResult))