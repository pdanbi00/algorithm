import sys
S = sys.stdin.readline().rstrip()

arr0 = S.split('1')
arr1 = S.split('0')
zero_cnt = len(arr0) - arr0.count('')
one_cnt = len(arr1) - arr1.count('')

print(min(one_cnt, zero_cnt))