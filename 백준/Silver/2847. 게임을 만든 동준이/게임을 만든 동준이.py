N = int(input())
scores = []
ans = 0
for i in range(N):
    n = int(input())
    scores.append(n)

# 마지막 레벨부터 처음 레벨까지 한개씩 확인
for i in range(N-1, 0, -1):
    if scores[i] <= scores[i-1]:
        # 점수를 앞의 점수와의 차이 + 1 만큼 감소. 그래야 1 작은 수 되니깐
        ans += (scores[i-1] - scores[i]) + 1
        # 앞 레벨은 지금보다 1 낮은 점수 부여
        scores[i-1] = scores[i] - 1

print(ans)