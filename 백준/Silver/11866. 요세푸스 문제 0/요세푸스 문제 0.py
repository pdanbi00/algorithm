# 두번째 방법
N, K = map(int, input().split())

# 요세푸스 순열 생성
idx = 0
nums = [i for i in range(1, N+1)]
result = []
while nums:
    idx += (K-1) # K-1번 인덱스까지 건너뛰기
    if idx >= len(nums): # 인덱스가 범위를 넘어가면
        idx %= len(nums) # 나머지 연산으로 줄여주기
    result.append(str(nums.pop(idx)))
print("<", ", ".join(result), ">", sep="")