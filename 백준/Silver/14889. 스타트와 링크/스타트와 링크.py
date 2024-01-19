N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

def func(index, start, link):
    if index == N:
        if len(start) != N//2:
            return -1
        if len(link) != N//2:
            return -1
        s_total = 0
        l_total = 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue
                s_total += powers[start[i]][start[j]]
                l_total += powers[link[i]][link[j]]
        return abs(s_total - l_total)

    if len(start) > (N//2) or len(link) > (N//2):
        return -1
    ans = -1
    s_total = func(index+1, start+[index], link)
    if ans == -1 or (s_total != -1 and ans > s_total):
        ans = s_total
    l_total = func(index+1, start, link+[index])
    if ans == -1 or (l_total != -1 and ans > l_total):
        ans = l_total
    return ans

print(func(0, [], []))

