import sys
input = sys.stdin.readline
N = int(input())
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)
# words.sort()
ans = []
ans_cnt = -1
for i in range(N-1):
    for j in range(i+1, N):
        word_cnt = 0
        for k in range(min(len(words[i]), len(words[j]))):
            # print(words[i], words[j], words[i][k], words[j][k], words[i][k] == words[j][k])
            if words[i][k] == words[j][k]:
                word_cnt += 1
                if word_cnt > ans_cnt:
                    ans_cnt = word_cnt
                    ans = [words[i], words[j]]
            else:
                # print(word_cnt)
                break
print(ans[0])
print(ans[1])