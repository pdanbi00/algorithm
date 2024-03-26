croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
line = input()
for c in croatia:
    line = line.replace(c, "a")
print(len(line))