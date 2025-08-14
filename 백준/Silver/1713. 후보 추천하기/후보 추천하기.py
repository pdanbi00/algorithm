N = int(input())
total = int(input())
recommend = list(map(int, input().split()))

dashboard = dict()

for i in range(total):
    if recommend[i] in dashboard.keys():
        dashboard[recommend[i]] += 1
    else:
        if len(dashboard) == N:
            min_value = total
            for key in reversed(dashboard.keys()):
                if min_value >= dashboard[key]:
                    min_value = dashboard[key]
                    min_key = key
            # 가장 오래된 값 삭제
            dashboard.pop(min_key)
            dashboard[recommend[i]] = 1
        else:
            dashboard[recommend[i]] = 1

sorted_keys = sorted(dashboard.keys())

print(*sorted_keys)