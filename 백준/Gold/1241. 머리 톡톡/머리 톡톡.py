N = int(input())
student = {}
nums = []
max_v = 0
for _ in range(N):
    i = int(input())
    max_v = max(max_v, i)
    nums.append(i)
    if i not in student:
        student[i] = 1
    else:
        student[i] += 1
arr = [0] * (max_v+1)

for k, v in student.items():
    for i in range(k, max_v+1, k):
        if k == i:
            arr[i] += v-1
        else:
            arr[i] += v

for n in nums:
    print(arr[n])