N = int(input())
words = []
index = {'a' : 1, 'b' : 2, 'k' : 3, 'd' : 4, 'e' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'l' : 9, 'm' : 10, 'n' : 11, 'c' : 12, 'o' : 13, 'p' : 14, 'r' : 15, 's' : 16, 't' : 17, 'u' : 18, 'w' : 19, 'y' : 20}

for _ in range(N):
    word = input()
    newWord = word.replace('ng', 'c')
    tmp = ''
    for i in range(len(newWord)):
        tmp += chr(96+index[newWord[i]])
    newWord = word.replace('c', 'ng')
    words.append((tmp, newWord))

words.sort()
# print(words)
for i in range(N):
    print(words[i][1])