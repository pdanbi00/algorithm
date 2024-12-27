# 4개를 골라서 2개씩 더한 합의 차이가 가장 작은 눈사람 찾기
# 미리 두개의 원소를 정하고, 해당 두 원소 사이에서 투포인터로 키 차이 최소값 차지

N = int(input())
snow = list(map(int, input().split()))
snow.sort()

answer = 1e9
for i in range(N-3):
    for j in range(i+3, N):
        anna = snow[i] + snow[j]

        left = i + 1
        right = j - 1
        while left < right:
            elsa = snow[left] + snow[right]
            diff = abs(anna - elsa)
            answer = min(answer, diff)
            if answer == 0:
                print(0)
                exit()
            if anna > elsa:
                left += 1
            else:
                right -= 1
            # # 정렬 된 상태이기 때문에 tmp < 0 인 경우는
            # # snow[left] + snow[right] > snow[i] + snow[j]
            # # tmp를 늘려야하기 때문에
            # if tmp < 0:
            #     right -= 1
            # # tmp > 0인 경우는
            # # snow[left] + snow[right] < snow[i] + snow[j]
            # # tmp를 줄여야하기 때문에
            # # (right + 1을 하지 않는 이유는 그러면 right의 범위가 j를 넘어갈 수 있어서)
            # else:
            #     left += 1

print(answer)