def solution(number, k):
    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -=1
            stack.pop()
            # print(stack)
            # print('---')
            # 들어오는 값이 stack값보다 크면 기본값 제거하고 새로운 값으로 바꾸도록
        stack.append(num)
        # print(stack)
        # print('***')
    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

# number = '4177252841'
# k = 4
# print(solution(number,k))
