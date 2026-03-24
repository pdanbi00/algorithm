N, C = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
# 최대 3개

def binary_search(left, right, diff):
    while left <= right:
        mid = (left + right) // 2
        if weight[mid] == diff:
            return 1
        elif weight[mid] > diff:
            right = mid - 1
        else:
            left = mid + 1
    return 0

def check(n, c):
    if c in weight:
        return 1
    i, j = 0, n-1

    while i < j:
        total = weight[i] + weight[j]
        if total > c:
            j -= 1
        elif total == c:
            return 1
        else:
            diff = c - total
            if binary_search(i+1, j-1, diff):
                return 1
            i += 1

if check(N, C):
    print(1)
else:
    print(0)