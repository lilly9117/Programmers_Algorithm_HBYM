#https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python

import math 

def solution(w, h):
    # 최대공약수
    g = math.gcd(w, h)

    # 빠지는 사각형 수
    minus = (w // g + h // g - 1) * g

    return w * h - minus