N = int(input())
hills = list(int(input()) for _ in range(N))
answer = 0

min_v = min(hills)
max_v = max(hills)

def cal(min, max):
    result = 0
    for i in range(N):
        tmp = 0
        if hills[i] > max:
            tmp = (hills[i] - max) ** 2
        elif hills[i] < min:
            tmp = (min - hills[i]) ** 2
        result += tmp
    return result

answer = 1e9
for i in range(min_v, max_v - 17):
    answer = min(answer, cal(i, i+17))
if answer == 1e9:
    print(0)
else:
    print(answer)