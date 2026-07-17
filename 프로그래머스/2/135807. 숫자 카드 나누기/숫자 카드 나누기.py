def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
        
    for i in range(len(arrayB)):
        if arrayB[i] % gcdA == 0:
            gcdA = 0
            break
            
    for i in range(len(arrayA)):
        if arrayA[i] % gcdB == 0:
            gcdB = 0
            break
    
    return max(gcdA, gcdB)

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)