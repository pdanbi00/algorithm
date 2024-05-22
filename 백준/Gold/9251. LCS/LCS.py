string1 = list(input())
string2 = list(input())
lcs = [[0]*(len(string2) + 1) for _ in range(len(string1) + 1)]
for i in range(1, len(string1)+1):
    for j in range(1, len(string2)+1):
        if string1[i-1] == string2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])