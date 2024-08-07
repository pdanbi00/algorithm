import sys
input = sys.stdin.readline

game = {'Y':2, 'F':3, 'O':4}

N, G = input().split()
N = int(N)
player = set()
for _ in range(N):
    person = input()
    player.add(person)
ans = len(player) // (game[G] - 1)
print(ans)