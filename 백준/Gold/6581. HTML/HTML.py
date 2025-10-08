import sys
txt = []
for line in sys.stdin:
    txt += line.split()

line = ''
for w in txt:
    if w == '<br>':
        print(line.rstrip())
        line = ''
    elif w == '<hr>':
        if line:
            print(line.rstrip())
        line = '-' * 80
        print(line)
        line = ''
    else:
        if len(line + w) > 80:
            print(line.rstrip())
            line = w + ' '
        else:
            line += w + ' '
if line:
    print(line.rstrip())