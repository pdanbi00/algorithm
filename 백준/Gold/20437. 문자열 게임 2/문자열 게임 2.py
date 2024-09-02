# 아이디어 : 문자열 전체 돌면서 각 문자 개수 세기
# 다시 문자열 돌면서 k개 이상인 문자의 인덱스 모두 저장
# 저장된 리스트에서 해당 문자 개수를 포함시켜서 최대 최소 갱신


T = int(input())
for _ in range(T):
    W = list(input())
    K = int(input())

    # 각 문자의 개수를 세는 딕셔너리
    count_char_dict = {}

    # 각 문자 개수 세기
    for char in W:
        count_char_dict[char] = count_char_dict.get(char, 0) + 1

    # 결과와 관련된 변수
    possible = False
    max_answer = -1
    min_answer = len(W)

    # 특정 문자열의 위치 index를 저장하는 딕셔너리
    idx_dict = {}

    # 모든 문자열에 대해서
    for i in range(len(W)):
        if count_char_dict[W[i]] < K:
            continue
        # k개 이상인 문자가 있으면 정답은 있는거임
        possible = True
        idx_dict[W[i]] = idx_dict.get(W[i], []) + [i]

    for key, values in idx_dict.items():
        for i in range(len(values) - K + 1):
            max_answer = max(max_answer, values[i + K - 1] - values[i] + 1)
            min_answer = min(min_answer, values[i + K - 1] - values[i] + 1)
            
    if possible:
        print(min_answer, max_answer)
    else:
        print(-1)