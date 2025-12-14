N = int(input())
data = list(map(int, input().split()))
cache = {}

def find_permutations(n):
    if n in cache:
        return cache[n]

    elif n <= 1:
        return 1

    else:
        cache[n] = n * find_permutations(n-1)
        return cache[n]

if data[0] == 1:
    k = data[1]
    arr = [i for i in range(1, N+1)]
    ans = []

    for i in range(N):
        x = find_permutations(N-1-i)
        step = (k-1) // x
        ans.append(arr[step])
        arr.remove(arr[step])
        k -= x * step

    print(*ans)

else:
    input_permu = data[1:]
    sorted_permu = sorted(input_permu)
    ans = 1

    for i in range(N):
        step = sorted_permu.index(input_permu[i])
        sorted_permu.remove(input_permu[i])
        x = find_permutations(N-1-i)
        ans += x * step

    print(ans)