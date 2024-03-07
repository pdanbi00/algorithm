N = int(input())
cnt = 0
for i in range(N):
    not_group_word = False
    words = input()
    alpha = []
    for j in range(len(words)):
        if words[j] not in alpha:
            alpha.append(words[j])
        else:
            if words[j] != words[j-1]:
                not_group_word = True
    if not not_group_word:
        cnt += 1
print(cnt)