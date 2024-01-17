import sys
nanjange = []
total = 0
for i in range(9):
    num = int(input())
    nanjange.append(num)
    total += num
nanjange.sort()
for i in range(8):
    for j in range(i+1, 9):
        if total - nanjange[i] - nanjange[j] == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                else:
                    print(nanjange[k])
            sys.exit(0)