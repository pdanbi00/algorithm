N = int(input())
book_dict = dict()
for _ in range(N):
    book = input()
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1

answer = []
max_cnt = 0
for k, v in book_dict.items():
    if v > max_cnt:
        max_cnt = v
        answer = [k]
    elif v == max_cnt:
        answer.append(k)

answer.sort()
print(answer[0])