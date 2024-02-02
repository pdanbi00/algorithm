import sys
print = sys.stdout.write
nums = [
    [1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1]
]

s, n = input().split()
s = int(s)
l = len(n)
for i in range(5):
    if i in [0, 2, 4]: # 가로로 표시되는 선들을 표시
        for j in range(l):
            now = int(n[j]) # 지금 표시해야할 숫자
            if j != 0:
                print(' ')
            print(' ') # 세로, 가로, 세로로 표시하니깐 세로가 들어올 칸은 빈칸으로 출력
            if (i == 0 and nums[now][0]) or (i == 2 and nums[now][3]) or (i == 4 and nums[now][6]):
                print('-'*s)
            else:
                print(' '*s)
            print(' ') # 세로, 가로, 세로로 표시하니깐 세로가 들어올 칸은 빈칸으로 출력
        print('\n')
    else:
        for k in range(s):
            for j in range(l):
                now = int(n[j])
                if j != 0:
                    print(' ')
                if (i == 1 and nums[now][1]) or (i == 3 and nums[now][4]):
                    print('|')
                else:
                    print(' ')
                print(' '*s)
                if (i == 1 and nums[now][2]) or (i == 3 and nums[now][5]):
                    print('|')
                else:
                    print(' ')
            print('\n')

