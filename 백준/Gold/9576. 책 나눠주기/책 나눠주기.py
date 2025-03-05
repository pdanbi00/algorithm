T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    books = []
    ans = 0
    for _ in range(M):
        a, b = map(int, input().split())
        books.append((a, b))

    books.sort(key=lambda x : (x[1], x[0]))
    check = [0] * (N+1)
    for i in range(M):
        for j in range(books[i][0], books[i][1]+1):
            if check[j] == 0:
                check[j] = 1
                ans += 1
                break

    print(ans)