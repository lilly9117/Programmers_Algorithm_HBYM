import re

def solution(files):
    answer = []
    file_list = [re.split('([0-9]+)',i) for i in files] #re.split 이용 구분자로해서 파일명 나눔

    file_list.sort(key = lambda x: (x[0].lower(), int(x[1]))) # 숫자 작은거 파일명 순으로 나열

    answer = [''.join(x) for x in file_list]

    return answer

# files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# print(solution(files))
