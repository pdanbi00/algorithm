import re

word = input()
pattern = re.compile('(100+1+|01)+')

res = pattern.fullmatch(word)

if res:
    print("SUBMARINE")
else:
    print("NOISE")