N = int(input())
nums = list(map(int, input().split()))

answer = 0

if N == 1:
    nums.sort()
    answer = sum(nums[:5])
else:
    # 1면만 나오는 갯수 : (N-2) * (N-2) + (4 * (N-2) * (N-1))
    # 2면만 나오는 갯수 : 4 * (N-2) + 4 * (N-1)
    # 3면만 나오는 갯수 : 4

    sumList = []
    sumList.append(min(nums[0], nums[5]))
    sumList.append(min(nums[1], nums[4]))
    sumList.append(min(nums[2], nums[3]))
    sumList.sort()

    min1 = sumList[0]
    min2 = sumList[0] + sumList[1]
    min3 = sumList[0] + sumList[1] + sumList[2]


    n1 = ((N-2) * (N-2)) + (4 * (N-1) * (N-2))
    n2 = (4 * (N-1) + 4 * (N-2))
    n3 = 4

    answer += min1 * n1
    answer += min2 * n2
    answer += min3 * n3

print(answer)