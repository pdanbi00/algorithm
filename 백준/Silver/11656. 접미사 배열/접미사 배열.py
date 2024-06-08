S = input()
words = []
for i in range(len(S)):
    words.append(S[i:len(S)])
words.sort()
for w in words:
    print(w)