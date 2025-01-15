N = int(input())
nums = list(map(int, input().split()))

# 첫번째, 두번째 원소에 대해서만 -1, 0, 1 연산을 다 고려해서 공차를 구함. 9가지
# 공차를 구하고 수열 나머지 부분도 해당하는 공차를 가지는 등차수열이 될 수 있는지 확인
# 한번이라도 등차수열 성립 안하면 검사 종료

def check(i, j):
    cnt = abs(i) + abs(j) # 연산횟수. 1번째, 2번째 원소 연산 횟수(-1, 1은 연산횟수 1이고, 0은 연산횟수 0)
    arr = []
    arr.append(nums[0] + i)
    arr.append(nums[1] + j)
    diff = nums[1] + j - (nums[0] + i) # 공차

    for k in range(2, N):
        if nums[k] == arr[k-1] + diff:
            arr.append(nums[k])
        elif nums[k] - 1 == arr[k-1] + diff:
            arr.append(nums[k] - 1)
            cnt += 1
        elif nums[k] + 1 == arr[k-1] + diff:
            arr.append(nums[k] + 1)
            cnt += 1
        else:
            return False
    return cnt

ans = 1e9

if N < 3: # 숫자가 1개이거나 2개면 공차는 구할 필요 없음
    print(0)
    exit()

for i in range(-1, 2): # 첫번째 원소에 적용할 연산
    for j in range(-1, 2): # 두번째 원소에 적용할 연산
        tmp = check(i, j)
        if tmp == False:
            continue
        else:
            ans = min(ans, tmp)

if ans == 1e9:
    print(-1)
else:
    print(ans)
