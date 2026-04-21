def back_tracking(cnt):
    # 현재 문자 길이가 입력된 문자 길이와 같으면 출력
    if cnt == len(word):
        print("".join(answer))
        return

    # 반복문으로 visited 단어 확인
    for k in alpha:
        if alpha[k]:
            alpha[k] -= 1 # 하나 사용했다는 표시
            answer.append(k)
            back_tracking(cnt+1)
            answer.pop()
            alpha[k] += 1

N = int(input())

for _ in range(N):
    word = sorted(list(input()))
    alpha = dict()
    answer = []

    # 각 알파벳이 몇개씩 있는지 확인
    for i in word:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1

    back_tracking(0)