def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))

    for p in range(len(phone_book)):
        for i in range(len(phone_book)):
            if p != i and phone_book[p] in phone_book[i][:len(phone_book[p])]:
                return False

    return True