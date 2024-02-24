text = input()
for i in range(0, len(text), 10):
    if len(text) >= i+10:
        print(text[i:i+10])
    else:
        print(text[i:])