# 하노이탑은 3단계로 구분 가능
# 첫번째 탑에 다 쌓여있을때
# 1. 마지막 원판 빼고 다 중간 탑으로 옮김
# 2. 마지막 원판을 제일 오른쪽 탑으로 옮김
# 3. 중간 탑에 있는 모든 원판을 제일 오른쪽 탑으로 옮김

N = int(input())

# n개의 원판을 몇번 막대에서 몇번 막대로 옮길 것인지
def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return
    # start 막대에 있는 n개의 원판 중 n-1개의 원판을 end가 아닌 2번 막대로 옮김
    # 1번 막대, 2번 막대, 3번 막대 번호를 합치면 6이니깐 6 - start - end 막대에 보낸다고 생각하면 됨

    hanoi_tower(n-1, start, 6 - start - end)
    print(start, end) # n번째 원판을 start에서 end로 옮기기
    hanoi_tower(n-1, 6 - start - end, end)

print(2 ** N - 1) # 총 움직인 횟수
hanoi_tower(N, 1, 3)
