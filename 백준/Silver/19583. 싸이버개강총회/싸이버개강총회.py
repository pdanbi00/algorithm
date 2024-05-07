import sys
input = sys.stdin.readline

S, E, Q = input().split()
S = int(S[:2]) * 60 + int(S[3:])
E = int(E[:2]) * 60 + int(E[3:])
Q = int(Q[:2]) * 60 + int(Q[3:])

attendance = set()
ans = 0
while True:
    try:
        time, name = input().split()
        time = int(time[:2]) * 60 + int(time[3:])
        if time <= S:
            attendance.add(name)
        elif E <= time <= Q and name in attendance:
            attendance.remove(name) # 한명이 여러 댓글 써도 하나의 사람으로만 인식해야하니깐
            ans += 1
    except:
        break
print(ans)