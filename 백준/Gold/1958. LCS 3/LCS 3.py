first = list(input())
second = list(input())
third = list(input())

LCS = [[[0] * (len(third)+1) for _ in range(len(second) + 1)] for _ in range(len(first)+1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        for k in range(1, len(third)+1):
            if first[i-1] == second[j-1] == third[k-1]:
                LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
            else:
                LCS[i][j][k] = max(LCS[i-1][j][k], LCS[i][j-1][k], LCS[i][j][k-1])
print(LCS[len(first)][len(second)][len(third)])