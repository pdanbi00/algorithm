N = int(input())
tree = {} # 각 key에 대한 자식 방에 대한 정보 담기
# 0B : 1A
# 0A : 1B, 1D
# 0A 1B : 2C
# 0A 1B 2C : 3D

for _ in range(N):
    arr = list(input().split())
    K = int(arr[0])
    food = arr[1:]
    if K == 1:
        tmp = str(0) + food[0]
        if tmp not in tree:
            tree[tmp] = set()
        tree[tmp].add('zzz')
    else:
        for i in range(K-1):
            tmp = ''
            for j in range(i):
                tmp += str(j) + food[j] + ' '
            tmp += str(i) + food[i]
            if tmp not in tree:
                tree[tmp] = set()
            tree[tmp].add(tmp + ' ' + str(i+1) + food[i+1])

def find(k):
    tmp_k = list(k.split())
    if tmp_k[-1][:2].isdigit():
        tmp = '--' * int(tmp_k[-1][:2])
        tmp += tmp_k[-1][2:]
    else:
        tmp = '--' * int(tmp_k[-1][:1])
        tmp += tmp_k[-1][1:]
    print(tmp)
    new_keys = [key for key in tree[k]]
    new_keys.sort(key=lambda x : (len(list(x.split())), x))

    for new_key in new_keys:
        if new_key in tree.keys():
            find(new_key)
        else:
            if new_key != 'zzz':
                new_tmp_k = list(new_key.split())
                if new_tmp_k[-1][:2].isdigit():
                    tmp = '--' * int(new_tmp_k[-1][:2])
                    tmp += new_tmp_k[-1][2:]
                else:
                    tmp = '--' * int(new_tmp_k[-1][:1])
                    tmp += new_tmp_k[-1][1:]
                print(tmp)
    return

tree_k = [k for k in tree.keys()]
tree_k.sort(key=lambda x : (len(list(x.split())), x))

for t_k in tree_k:
    k = list(t_k.split())
    if len(k) == 1:
        find(t_k)