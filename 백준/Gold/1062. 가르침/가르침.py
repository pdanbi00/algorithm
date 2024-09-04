import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# K가 5보다 작으면 어떤 언어도 배울 수 없음. anta tica만 해도 5글자여서
if K < 5:
    print(0)
    exit()

# K가 26이면 모든 단어 배울 수 있음
elif K == 26:
    print(N)
    exit()

answer = 0
words = [set(input().rstrip()) for _ in range(N)]
learn = [0] * 26

# 최소 단어 하나를 배우기 위해서는 a, c, i, n, t 무조건 배워야 됨.
for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def check():
    read_cnt = 0
    for word in words:
        check = True # 배운 글자로 단어 읽을 수 있는지 확인
        for w in word:
            if not learn[ord(w) - ord('a')]:
                check = False
                break
        if check:
            read_cnt += 1
    return read_cnt

def dfs(idx, deepth):
    global answer
    
    if deepth == K-5:
        answer = max(answer, check())
        return
    
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, deepth+1)
            learn[i] = 0

dfs(0, 0)
print(answer)