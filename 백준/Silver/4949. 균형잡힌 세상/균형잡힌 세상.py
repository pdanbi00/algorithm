while True:
    text = input()
    gwalho = []
    if text == '.':
        break
    for t in text:
        if t == '(' or t == '[':
            gwalho.append(t)
        elif t == ')':
            if gwalho and gwalho[-1] == '(':
                gwalho.pop()
            else:
                print("no")
                break
        elif t == ']':
            if gwalho and gwalho[-1] == '[':
                gwalho.pop()
            else:
                print("no")
                break
    else:
        if not gwalho:
            print("yes")
        else:
            print("no")