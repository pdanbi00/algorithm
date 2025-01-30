import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    phone = [input().rstrip() for _ in range(n)]

    phone.sort()
    answer = True

    for i in range(n-1):
        if len(phone[i]) <= len(phone[i+1]):
            if phone[i] == phone[i+1][:len(phone[i])]:
                answer = False
                break
    if answer:
        print("YES")
    else:
        print("NO")