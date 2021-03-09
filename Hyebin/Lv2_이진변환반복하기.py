def solution(s):
    # answer = []
    count = 0
    zero = 0

    while True:
        if s == '1':
            break
        else:
            zero += s.count('0')
            s = s.replace('0','')
            s = bin(len(s))[2:]
            count+=1
    
    answer = [count,zero]
    return answer

# s = "110010101001"
# print(solution(s))