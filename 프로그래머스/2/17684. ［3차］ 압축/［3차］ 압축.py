# 아이디어 : 종이에 적어서 풀어보면 너는 알고리즘을 구현해낼 수 있음. 오늘의 내가 해냈기 때문에
def solution(msg):
    answer = []
    alpha = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
    }
    cnt = 27
    idx = 0
    word = ''
    while idx < len(msg):
        word += msg[idx]
        if word in alpha.keys():
            idx += 1

        else:
            answer.append(alpha[word[:-1]])
            alpha[word] = cnt
            cnt += 1
            word = ''

    answer.append(alpha[word])

    return answer