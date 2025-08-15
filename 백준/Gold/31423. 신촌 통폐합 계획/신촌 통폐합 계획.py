import sys
input = sys.stdin.readline
N = int(input())
schools = [""]
for _ in range(N):
    school = input().rstrip()
    schools.append(school)

nextIdx = [i for i in range(N+1)] # 바로 다음에 오는 인덱스의 대학
lastIdx = [i for i in range(N+1)] # 각 인덱스의 마지막 대학

'''
i번째 문자가 a,a',a"이고
j번째 문자가 b,b'이면
a,a',a",b,b'가 되어야 됨
a",즉 i번째 문자의 마지막 인덱스 lastIdx[i]의 다음 인덱스는 b여야 됨.
그리고 a의 마지막 인덱스 lastIdx[i]를 b의 마지막 인덱스(b')로 설정해야하기 때문에
lastIdx[a] = lastIdx[b]로 설정
'''

for _ in range(N-1):
    i, j = map(int, input().split())
    nextIdx[lastIdx[i]] = j
    lastIdx[i] = lastIdx[j]

result = []
for _ in range(N):
    result += schools[i]
    i = nextIdx[i]
print("".join(result))