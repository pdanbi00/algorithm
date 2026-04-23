T = int(input())
for _ in range(T):
    M, N = input().split()
    if M == '1':
        ans = ''
        ip = list(map(int, N.split('.')))
        for p in ip:
            ans += bin(p)[2:].zfill(8)
        print(int(ans, 2))

    else:
        ans = ''
        ip = str(bin(int(N))[2:]).zfill(64)
        for i in range(8):
            ans += str(int(ip[i*8:(i+1)*8], 2))
            if i != 7:
                ans += '.'
        print(ans)
