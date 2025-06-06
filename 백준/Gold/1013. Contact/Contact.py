import sys
input = sys.stdin.readline

T = int(input())
# (100+1+ | 01) +
for _ in range(T):
    s = input().rstrip()
    result = True

    while len(s) > 0:
        if s.startswith("100"):
            s = s[3:] # 100 제거
            while len(s) > 0 and s.startswith("0"): # 0+ 0이 계속 나오는 경우
                s = s[1:] # 0 제거
            if len(s) == 0: # 뒤에 "1"이 하나는 무조건 있어야하니깐 False
                result = False
                break

            s = s[1:] # 맨 처음에 "1" 나오는 경우 1 제거
            # 이까지 하면 100+ 1까지 만족
            while len(s) > 0 and s.startswith("1"):
                if len(s) >= 3 and s[1] == "0" and s[2] == "0": # "100"이 나오는 경우일수도 있으니깐 보류
                    break
                else:
                    s = s[1:]

        elif s.startswith("01"):
            s = s[2:] # "01" 제거
        else:
            result = False
            break

    if result:
        print("YES")
    else:
        print("NO")