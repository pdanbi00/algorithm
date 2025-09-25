# dfs임
# 기준점부터 뒤쪽 완성 다 시키고
# 그 다음에 기준점 앞쪽 완성시키는거 반복

import sys
sys.setrecursionlimit(10**6)

line = list(input())
N = len(line)
word = []
used = [False] * N

def func(s, e): # 시작 인덱스, 종료 인덱스, 뒤에 붙여야하는지 여부(True면 뒤에 붙이기 False면 앞에 추가하기)
    global answer, used, word
    if s <= e and 0 <= s < N and 0 <= e < N:
        # 가장 작은 위치 확인하기
        small = ord(line[s])
        small_idx = s

        for i in range(s+1, e+1):
            if ord(line[i]) < small:
                small = ord(line[i])
                small_idx = i
        if used[small_idx] == False:
            word.append(small_idx)
            used[small_idx] = True
            word.sort()
            tmp = ''
            for i in word:
                tmp += line[i]
            print(tmp)

            # 뒤쪽 확인하기
            func(small_idx+1, e)

            # 앞쪽 확인하기
            func(s, small_idx-1)

    return

func(0, N-1)