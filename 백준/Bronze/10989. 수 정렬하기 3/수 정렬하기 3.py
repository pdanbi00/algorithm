import sys
input = sys.stdin.readline

N = int(input())
# 메모리 제한이 있어서 리스트 크기를 제한해줌
list = [0] * 10001
# 숫자가 만약 3이라면 list[3]에 갯수가 하나씩 올라감
# 그래서 최종적으로 0번 인덱스부터 100001번 인덱스까지 다 돌면서
# list[숫자]에 해당하는 수 만큼 숫자를 출력 해주면 됨.
for i in range(N):
    list[int(input())] += 1

# 리스트 전체 다 돌아야됨.
# N 만큼 돌면 숫자는 1400 이런거 들어와도 N이 5면 4번 인덱스까지 밖에 안 보니깐 안됨.
for i in range(10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)
