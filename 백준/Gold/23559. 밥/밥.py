import sys
input = sys.stdin.readline

N, X = map(int, input().split())
# 다 천원짜리로 한거랑 몇개 5천원 섞은거랑 비교
# A, B의 차이가 큰 순서대로 정렬해서 제일 클 때부터 5천원 선택
answer = 0
foods = []
for i in range(N):
    A, B = map(int, input().split())
    foods.append((A, B, A-B))
    answer += B # 일단 다 천원 짜리로 사는 경우를 정답으로 둠
foods.sort(key = lambda x : (x[2], x[0], x[1]), reverse=True)
X -= 1000 * N

# 천원짜리로 사고 돈이 남아있고, 5천원짜리가 천원짜리보다 가치가 크면 추가
for food in foods:
    if X >= 4000 and food[2] > 0:
        answer += food[0] - food[1]
        X -= 4000
    else:
        break
print(answer)