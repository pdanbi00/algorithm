L, C = map(int, input().split())
alphabets = input().split()
alphabets.sort()

def check(password):
    mo = 0
    ja = 0
    for a in password:
        if a in 'aeiou':
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        return True
    else:
        return False

def func(password, index, L):
    if len(password) == L:
        if check(password):
            print(password)
            return
    if index == len(alphabets):
        return
    func(password+alphabets[index], index+1, L)
    func(password, index+1, L)

func('', 0, L)