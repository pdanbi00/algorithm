import sys
input = sys.stdin.readline
K, L = map(int, input().split())
student = {}
again_student = {}
answer = []
for i in range(1, L+1):
    s = input()
    student[s] = i
for k, v in student.items():
    answer.append((v, k))
answer.sort(key=lambda x : x[0])
for i in range(K):
    try:
        print(answer[i][1], end='')
    except:
        exit()