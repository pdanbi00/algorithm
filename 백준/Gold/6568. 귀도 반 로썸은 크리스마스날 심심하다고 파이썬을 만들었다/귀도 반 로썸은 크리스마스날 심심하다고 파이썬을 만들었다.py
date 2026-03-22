import sys
input = sys.stdin.readline
while True:
    try:
        memory = [0] * 32
        # 메모리에 먼저 저장
        for i in range(32):
            memory[i] = int(input().strip(), 2)
        pc = 0
        alu = 0
        while True:
            cmd = memory[pc] // 32
            num = memory[pc] % 32
            pc = (pc+1) % 32
            if cmd == 0:
                memory[num] = alu
            elif cmd == 1:
                alu = memory[num]
            elif cmd == 2:
                if alu == 0:
                    pc = num

            elif cmd == 3:
                continue
            elif cmd == 4:
                alu = (alu - 1) % 256
            elif cmd == 5:
                alu = (alu + 1) % 256
            elif cmd == 6:
                pc = num
            elif cmd == 7:
                break

        print(bin(alu)[2:].zfill(8))
    except:
        break