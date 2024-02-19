# 이것은 누가봐도 스택~~
while True:
    text = input()
    if text == '.':
        break
    else:
        gwalho = []
        possible = True
        for t in text:
            if t == '(' or t == '[':
                gwalho.append(t)
            elif t == ')':
                if gwalho:
                    next = gwalho.pop()
                    if next != '(':
                        print("no")
                        possible = False
                        break
                else:
                    print("no")
                    possible = False
                    break
            elif t == ']':
                if gwalho:
                    next = gwalho.pop()
                    if next != '[':
                        print("no")
                        possible = False
                        break
                else:
                    print("no")
                    possible = False
                    break
        if possible and not gwalho:
            print("yes")
        elif possible and gwalho:
            print("no")
