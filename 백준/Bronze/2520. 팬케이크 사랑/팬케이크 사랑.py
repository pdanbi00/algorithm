T = int(input())
for _ in range(T):
    empty = input()
    cm, y, su, sa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())
    cm *= 2
    y *= 2
    su *= 4
    sa *= 16
    f = int(f * (16 / 9))
    pan = min(cm, y, su, sa, f)
    gs //= 30
    gc //= 25
    w //= 10
    tmp = b + gs + gc + w
    if pan < tmp:
        print(pan)
    else:
        print(tmp)