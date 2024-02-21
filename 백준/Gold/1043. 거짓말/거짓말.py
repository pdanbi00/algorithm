N, M = map(int, input().split())
knowList = set(input().split()[1:])
parties = []

for i in range(M):
    parties.append(set(input().split()[1:]))

# 진실 알게 되는 모든 사람 구하기
for i in range(M): # A 라는 사람이 진실을 알고 5개의 파티가 있다면 이 사람이 3번째 파티에 참여하고 B까지 진실을 알게 되면 B도 5개의 파티 중에 어디에 참여하는지 확인해야하니깐 새로운 사람이 진실 알게 되는 경우의 최대값은 매 파티마다 진실 알게되는 사람이 생기는거임.
    for party in parties:
        if party & knowList: # 파티에 참석 한 사람이랑 진실을 알고 있는 사람들의 교집합이 한명이라도 있으면 합집합으로 변경
            knowList = knowList.union(party)

cnt = 0
# 진실 아는 사람 다 구했으니깐 이제 확실하게 거짓말 할 수 있는지 아닌지 판단
for party in parties:
    if party & knowList:
        continue
    cnt += 1
print(cnt)