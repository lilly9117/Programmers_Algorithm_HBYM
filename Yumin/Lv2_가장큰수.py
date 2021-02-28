# https://huidea.tistory.com/4

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x: x * 3)[::-1]

    return str(int(''.join(map(str, numbers))))
    # str(int( - for ['0','0','0','0']

# fail - 30 3
# def solution(numbers):
#     numbers= sorted(numbers, key= lambda x: int(str(x)[0]))[::-1]
#     print(numbers)
#     return ''.join(map(str,numbers))