def solution(a, b):
    answer = ''
    last_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    week = ['FRI','SAT','SUN','MON', 'TUE','WED','THU']
    answer = week[(sum(last_day[:a-1])+b-1)%7]
    return answer

