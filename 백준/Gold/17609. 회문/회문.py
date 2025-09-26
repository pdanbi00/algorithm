import sys
input = sys.stdin.readline

def func(word):
    N = len(word)
    pseudo = False
    front = False
    back = False
    front_cnt = 0
    back_cnt = 0
    cnt = 0
    for i in range(N//2):
        if not pseudo:
            if word[i] == word[N-1-i]:
                cnt += 1
            else:
                if word[i] == word[N-1-i-1]:
                    pseudo = True
                    back = True
                    back_cnt = cnt + 1
                if word[i+1] == word[N-1-i]:
                    pseudo = True
                    front = True
                    front_cnt = cnt + 1

        else:
            if back:
                if word[i] == word[N - 1 - i -1]:
                    back_cnt += 1

            if front:
                if word[i+1] == word[N-1-i]:
                    front_cnt += 1

    if cnt == N//2 and not pseudo:
        return 0
    elif (front or back) and (front_cnt == N//2 or back_cnt == N//2) :
        return 1
    return 2

T = int(input())
for _ in range(T):
    word = list(input().rstrip())
    print(func(word))

'''
1
abaab
'''