def solution(brown, yellow):
    answer = []
    # yellow = xy - 2(x+y) + 4
    # brown = 2(x+y) -4
    # yellow + brown = xy
    #  방정식 풀면
    x = ((brown + 4) + ((brown + 4)**2 - 16*(brown+ yellow))**(1/2)) / 4
    y = (brown + yellow) / x
    answer = [int(max(x,y)), int(min(x,y))]
    return answer

# brown = 10
# yellow = 2
# print(solution(brown, yellow))