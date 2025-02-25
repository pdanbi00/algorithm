# 백트래킹
# 1부터 3까지 순서대로 수열 뒤에 붙이면서 좋은 수열인지 확인
N = int(input())
result = []

def good_num(result, count):
    for i in range(1, count//2 + 1):
        if str(result)[-i:] == str(result)[-2 * i:-i]:
            return

    if count == N:
        print(result)
        exit()

    for i in range(1, 4):
        temp = result * 10 + i
        good_num(temp, count + 1)

good_num(0, 0)