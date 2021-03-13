def solution(n, words):
    answer = [0,0]
    count = 1
    for i in range(1,len(words)):
        count %= n 
        if words[i] in words[0:i] or words[i-1][-1] != words[i][0]:
            answer = [count+1, i//n+1]
            return answer
        count+=1
    return answer

# n = 3
# words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
# print(solution(n,words))

