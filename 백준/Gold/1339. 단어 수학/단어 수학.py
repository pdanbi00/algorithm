N = int(input())
words = [input() for _ in range(N)]
alpha = {}
for word in words:
    x = len(word) - 1 # 10 몇제곱 할지
    for w in word:
        if w in alpha:
            alpha[w] += 10 ** x
        else:
            alpha[w] = 10 ** x
        x -= 1
arr = sorted(alpha.values(), reverse = True)
ans = 0
num = 9
for k in arr:
    ans += k * num
    num -= 1
print(ans)

# https://edder773.tistory.com/97