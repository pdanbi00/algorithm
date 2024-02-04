N = int(input())
words = [input() for _ in range(N)]
words = set(words)
words = list(words)

words.sort()
# words.sort(key=lambda x: len(x))
# sort의 key는 함수를 받기 때문에
words.sort(key=len) # 이렇게 하면 됨
for w in words:
    print(w)