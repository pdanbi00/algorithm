N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = [] # 제거된 사람들 넣을 배열
num = 0 # 제거될 사람의 인덱스 번호
for i in range(N):
    num += K-1
    if num >= len(arr):
        num %= len(arr)
    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep="")