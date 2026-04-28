# def solution(n):
#     answer = 0
#     for i in range(6, 6 * n+1):
#         if i % n == 0 and i % 6 == 0:
#             answer = i // 6
#             break
#     return answer
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solution(n):
    answer = 0
    answer = n * 6 // gcd(n, 6)
    return answer // 6