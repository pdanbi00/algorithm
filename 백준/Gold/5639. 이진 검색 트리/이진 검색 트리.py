# 제일 앞에 있는 수가 루트 노드, 뒤에 있는 배열에서 루트보다 작은 수까지가 왼쪽 배열, 나머지는 오른쪽 배열
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []

while True:
    try:
        a = int(input())
        arr.append(a)
    except:
        break

def func(A):
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
        tempL = A[1:]

    # 후위순회니깐 왼쪽, 오른쪽, 루트
    func(tempL)
    func(tempR)
    print(mid)

func(arr)