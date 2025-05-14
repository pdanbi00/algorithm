import sys
input = sys.stdin.readline
S = list(input().rstrip())
q = int(input().rstrip())

count = [[0] * 26]
for i in range(len(S)):
    count.append(count[len(count)-1][:])
    count[i+1][ord(S[i])-97] += 1

for _ in range(q):
    target, s, e = input().rstrip().split()
    answer = count[int(e)+1][ord(target)-97] - count[int(s)][ord(target)-97]
    print(answer)