from itertools import product

def solution(word):
    answer = 0
    arr = []
    for i in range(1, 6):
        for p in product('AEIOU', repeat=i):
            arr.append(''.join(p))
    arr.sort()
    
    return arr.index(word) + 1