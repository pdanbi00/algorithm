import sys
txt = []
for line in sys.stdin:
    txt += line.split()
count = 0
for w in txt:
    if w == "<br>":
        print()
        count = 0
    elif w == "<hr>":
        if count != 0:
            print()
        line = '-' * 80
        print(line)
        count = 0
    else:
        if count + len(w) + 1 > 80:
            print()
            count = 0
        elif count > 0:
            print(end=" ")
            count += 1
        print(w, end="")
        count += len(w)