N = int(input())
ans = 0
start = 1
length = 1
# 1부터 9까지는 1자리수, 10부터 99까지는 2자리수, 100부터 999까지는 3자리수 요런 느낌

while start <= N:
    end = start * 10 - 1
    if end > N:
        end = N
    ans += length * (end - start + 1)
    start *= 10
    length += 1
print(ans)