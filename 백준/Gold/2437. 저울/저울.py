'''
풀이
N개의 저울추 중에서 몇가지를 뽑아서 K만큼의 무게를 모두 측장할 수 있다고 가정
무게 X인 추를 새로 추가한다면 새로 측정할 수 있는 무게는 (1+X) ~ (K+X)rk rhla
이런 단계를 거칠때마다 K는 현재까지의 모든 추의 합이 됨.(현재까지의 모든 추를 다 합치면 최대값인 K니까)

근데 만약 추가되는 추 무게가 K+1보다 크다면 K+1이 비어버림

'''

N = int(input())
chu = list(map(int, input().split()))
chu.sort()

target = 1
for num in chu:
    if target < num:
        break

    target += num

print(target)