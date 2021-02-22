# def compare_f(a,b):
    

def solution(numbers):
    answer = ''
    n = [str(i) for i in numbers]
    # print(n)
    n.sort(key = lambda x : x*3, reverse=True)
    # print(n)

    if len(n) == n.count('0'):
        return '0'
    else:
        return ''.join(n)

