import sys
input = sys.stdin.readline
N, M = map(int, input().split())
words = []
words_dict = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

for k, v in words_dict.items():
    words.append((v, len(k), k))

words.sort(key=lambda x : (-x[0], -x[1], x[2]))
for i in range(len(words)):
    print(words[i][2])
