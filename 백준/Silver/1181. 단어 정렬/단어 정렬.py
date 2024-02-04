N = int(input())
words = [input() for _ in range(N)]
words = set(words)
words = list(words)

words.sort()
words.sort(key=lambda x: len(x))
for w in words:
    print(w)