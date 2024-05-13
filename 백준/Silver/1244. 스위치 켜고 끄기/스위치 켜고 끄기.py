N = int(input())
switch = list(map(int, input().split()))
student = int(input())
for i in range(student):
    sex, num = map(int, input().split())
    k = num
    if sex == 1:
        while num <= N:
            switch[num-1] = (switch[num-1] + 1) % 2
            num += k
    else:
        k = 1
        num -= 1
        switch[num] = (switch[num] + 1) % 2
        while num + k < N and num-k >= 0:
            if num+k < N and num-k >= 0 and switch[num + k] == switch[num - k]:
                switch[num+k] = (switch[num+k] + 1) % 2
                switch[num-k] = (switch[num-k] + 1) % 2
                k += 1
            else:
                break
for i in range(N):
    if i % 20 == 19:
        print(switch[i])
    else:
        print(switch[i], end=' ')

'''
25
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1
1 1
'''