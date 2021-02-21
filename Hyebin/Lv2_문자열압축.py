#sol : https://copy-driven-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-ProgrammersPython-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%95%95%EC%B6%95
def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1
    
    for cut in range(1, len(s)//2+1):
        count = 1
        tempstr = s[:cut]

        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempstr:
                count +=1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempstr
                tempstr = s[i:i+cut]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tempstr
        length.append(len(result))
        result = ""

    return min(length)