import sys
input = sys.stdin.readline
N = int(input())
dictionary1 = dict() # 한글자 정보
dictionary2 = dict() # 두 글자 이상 정보

# (a, c) : [0, 0, 3 ..., 2, 0] : 3
for _ in range(N):
    word = input().rstrip()
    if len(word) == 1:
        dictionary1[word[0]] = 1
    else:
        k = (word[0], word[-1])
        used = [0] * 52
        for i in range(1, len(word)-1):
            # print(word[i].lower())
            n = ord(word[i]) - ord('a')
            used[n] += 1
        used = tuple(used)
        if k not in dictionary2:
            dictionary2[k] = dict()
            dictionary2[k][used] = 1
        else:
            if used not in dictionary2[k]:
                dictionary2[k][used] = 1
            else:
                dictionary2[k][used] += 1
M = int(input())
for _ in range(M):
    if N == 0 or M == 0:
        print(0)
    else:
        impossible = 0
        line = list(input().rstrip().split())
        cnt = 1
        for i in range(len(line)):
            w = line[i]
            if len(w) == 1:
                if w[0] in dictionary1:
                    cnt *= 1
                else:
                    impossible += 1
            else:
                used = [0] * 52
                for j in range(1, len(w)-1):
                    used[ord(w[j]) - ord('a')] += 1
                used = tuple(used)
                # print(dictionary[(w[0], w[-1])][used])
                if (w[0], w[-1]) in dictionary2 and used in dictionary2[(w[0], w[-1])]:
                    cnt *= dictionary2[(w[0], w[-1])][used]
                else:
                    impossible += 1
        if impossible == len(line):
            cnt = 0
        print(cnt)