T = int(input())
for _ in range(T):
    line = list(input().split())
    answer = ""
    for i in range(len(line)):
        tmp = line[i][::-1]
        if i != len(line)-1:
            answer += tmp + " "
        else:
            answer += tmp
    print(answer)