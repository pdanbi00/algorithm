'''
로직
1. A랑 B를 앞에서부터 틀린 부분 찾기 s
2. A랑 B를 뒤에서부터 틀린 부분 찾기 e
3. A랑 B 중 짧은 길이에서 e를 뺀게 동일하지 않은 부분의 마지막 인덱스.
    근데 이 값이 s보다 크면 B의 길이에서 (e + s)를 뺀게 답
    그렇지 않다면(s보다 작거나 같다면) A의 길이가 더 길다면 0, 아니면 B의 길이 - A의 길이
'''

a = input()
b = input()
s = 0
min_l = min(len(a), len(b))
while s < min_l and a[s] == b[s]:
    s += 1

e = 0
while e < min_l and (a[len(a) - 1 - e] == b[len(b) - 1 - e]):
    e += 1

if s >= min_l - e:
    if len(a) > len(b):
        print(0)
    else:
        print(len(b) - len(a))
else:
    print(len(b) - s - e)