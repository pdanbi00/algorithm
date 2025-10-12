T = int(input())
for _ in range(T):
    crying = list(input().split())
    while True:
        sound = input()
        if sound == 'what does the fox say?':
            break
        sound = sound.split()
        while sound[2] in crying:
            crying.remove(sound[2])
    print(" ".join(crying))