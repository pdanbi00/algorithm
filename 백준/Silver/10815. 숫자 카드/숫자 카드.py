import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
nums = list(map(int, input().split()))

answer = []

def check(num):
    l = 0
    r = len(card) - 1

    while l <= r:
        mid = (l+r) // 2

        if card[mid] == num:
            return 1
        else:
            if card[mid]>= num:
                r = mid - 1
            else:
                l = mid + 1
    return 0

for n in nums:
    print(check(n), end=" ")
