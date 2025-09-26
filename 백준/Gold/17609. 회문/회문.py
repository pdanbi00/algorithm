import sys
input = sys.stdin.readline

def func(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            rm_left = word[left+1:right+1]
            if rm_left == rm_left[::-1]:
                return 1

            rm_right = word[left:right]
            if rm_right == rm_right[::-1]:
                return 1

            return 2
        left += 1
        right -= 1

    return 0

T = int(input())
for _ in range(T):
    word = list(input().rstrip())
    print(func(word))