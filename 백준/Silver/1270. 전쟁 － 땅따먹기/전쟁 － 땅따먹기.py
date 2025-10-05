# 보이어-무어 과반수 투표 알고리즘
def boyer_moore_majority(arr):
    count = 0 # 과반수의 원소가 몇개 있는지
    major = 0 # 과반수의 원소
    for ele in arr:
        if count == 0:
            major = ele
        if major == ele:
            count += 1
        else:
            count -= 1

    if count == 0:
        return None, None

    K = len(arr)
    m = 0 # 정말 과반수인지 체크용 변수

    for ele in arr:
        if ele == major:
            m += 1

    if m > K//2:
        return major, m

    else:
        return None, None


N = int(input())
for _ in range(N):
    war = list(map(int, input().split()))
    major_num, major_cnt = boyer_moore_majority(war[1:])
    if major_num == None:
        print("SYJKGW")
    else:
        print(major_num)