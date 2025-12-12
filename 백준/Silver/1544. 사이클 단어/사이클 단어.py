N = int(input())
words = [input() for _ in range(N)]

word_set = set()

for i in range(N):
    if not word_set:
        word_set.add(words[i])
    else:
        possible = True
        for j in range(len(words[i])):
            new_word = words[i][j:] + words[i][:j]
            # print(new_word)
            if new_word in word_set:
                possible = False
                break

        if possible:
            word_set.add(words[i])

print(len(word_set))