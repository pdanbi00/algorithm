H, W = map(int, input().split())
N = int(input())
arr = list([0] * 3 for _ in range(N))
for i in range(N):
   arr[i][0], arr[i][1] = map(int, input().split())
   arr[i][2] = arr[i][0] * arr[i][1]
arr.sort(reverse=True, key=lambda x : x[2])
max_v = 0
for i in range(N-1):
    for j in range(i+1, N):
        if arr[i][2] + arr[j][2] < max_v:
            break
        else:
            # 가 X 가
            if arr[i][0] + arr[j][0] <= W and arr[i][1] <= H and arr[j][1] <= H: # 가로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            elif arr[i][1] + arr[j][1] <= H and arr[i][0] <= W and arr[j][0] <= W: # 세로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            # 가 X 세
            elif arr[i][0] + arr[j][1] <= W and arr[i][1] <= H and arr[j][0] <= H: # 가로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            elif arr[i][1] + arr[j][0] <= H and arr[i][0] <= W and arr[j][1] <= W: # 세로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            # 세 X 가
            elif arr[i][1] + arr[j][0] <= W and arr[i][0] <= H and arr[j][1] <= H: # 가로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            elif arr[i][0] + arr[j][1] <= H and arr[i][1] <= W and arr[j][0] <= W: # 세로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            # 세 X 세
            elif arr[i][1] + arr[j][1] <= W and arr[i][0] <= H and arr[j][0] <= H: # 가로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
            elif arr[i][0] + arr[j][0] <= H and arr[i][1] <= W and arr[j][1] <= W: # 세로로 이어붙이는 경우
                max_v = max(max_v, arr[i][2]+arr[j][2])
                break
print(max_v)