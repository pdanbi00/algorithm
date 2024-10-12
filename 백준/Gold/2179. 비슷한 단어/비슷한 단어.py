import sys
input = sys.stdin.readline

# 문자열을 정렬시키면 가장 긴 접두사를 갖고 있는 문자끼리 붙게 됨(바로 앞 문자열이랑 비교했을 때 가장 긴 접두사의 길이를 낼 수 있음 와우)
N = int(input())
words = [input().rstrip() for _ in range(N)]

# 입력받은 문자열들을 인덱스랑 같이 사전 순으로 정렬
sorted_words = sorted(list(enumerate(words)), key=lambda x : x[1])

# 함수 글자 하나하나 같은지 탐색
def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            cnt += 1
        else:
            break
    return cnt
# 최장 접두사를 가진 문자열을 담아줄 리스트
length = [0] * (N+1)
max_length = 0

for i in range(N-1):
    # 인접한 문자열 2개를 check함수에 대입
    tmp = check(sorted_words[i][1], sorted_words[i+1][1])
    max_length = max(max_length, tmp)

    length[sorted_words[i][0]] = max(length[sorted_words[i][0]], tmp)
    length[sorted_words[i+1][0]] = max(length[sorted_words[i+1][0]], tmp)

first = 0
for i in range(N):
    # 입력된 순서대로 접두사 길이 비교
    if first == 0:
        if length[i] == max(length):
            first = words[i]
            print(first)
            pre = words[i][:max_length]
    else:
        if length[i] == max(length) and words[i][:max_length] == pre:
            print(words[i])
            break