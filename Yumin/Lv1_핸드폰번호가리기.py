def solution(phone_number):
    # 4자리 제외한 *
    x = '*' * (len(phone_number) - 4)
    # 뒷4자리
    y = ''.join(list(phone_number)[-4:])
    
    return ''.join([x, y])