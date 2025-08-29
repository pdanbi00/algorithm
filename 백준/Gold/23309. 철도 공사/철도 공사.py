import sys
import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
ans = __pypy__.builders.StringBuilder()
def main():
    N, M = map(int, input().split())
    stations_list = list(map(int, input().split()))

    prv = [0 for _ in range(1_000_000 + 1)]
    nxt = [0 for _ in range(1_000_000 + 1)]

    for i in range(N):
        now_station_num = stations_list[i]
        prv[now_station_num] = stations_list[i-1]
        nxt[now_station_num] = stations_list[(i + 1) % N]

    # A > B > C -> A > B > D > C
    def insert(B, D):
        C = nxt[B]
        nxt[B] = D
        prv[D], nxt[D] = B, C
        prv[C] = D

    # A > B > C -> A > C
    def remove(B):
        A, C = prv[B], nxt[B]
        nxt[A] = C
        prv[C] = A

    for _ in range(M):
        command = input().split()
        if command[0] == b'BN':
            i, j = int(command[1]), int(command[2])
            ans.append(str(nxt[i]) + '\n')
            insert(i, j)
        elif command[0] == b'BP':
            i, j = int(command[1]), int(command[2])
            ans.append(str(prv[i]) + '\n')
            insert(prv[i], j)
        elif command[0] == b'CN':
            i = int(command[1])
            ans.append(str(nxt[i]) + '\n')
            remove(nxt[i])
        else:
            i = int(command[1])
            ans.append(str(prv[i]) + '\n')
            remove(prv[i])

    os.write(1, ans.build().encode())


if __name__ == '__main__':
    main()