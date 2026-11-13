import math


def solution(w, h):
    # 전체 면적에서 대각선이 지나는 사각형의 개수를 뺀다
    return w * h - (w + h - math.gcd(w, h))