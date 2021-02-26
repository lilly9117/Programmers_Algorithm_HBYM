# 시간초과,,,

def solution_1(phone_book):
    
    answer = True

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].find(phone_book[i]) == 0 or phone_book[i].find(phone_book[j]) == 0:
                answer = False
                break
    
    return answer


def solution(phone_book):
    
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
    
    return answer

# phone_book = ["119", "97674223", "1195524421"]
# print(solution(phone_book))

# startswitch 함수도 사용가능!!!!!!