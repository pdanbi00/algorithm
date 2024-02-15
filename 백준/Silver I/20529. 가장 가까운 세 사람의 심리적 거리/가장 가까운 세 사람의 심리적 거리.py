T = int(input())
for tc in range(T):
    N = int(input())
    mbti = input().split()
    mbtis = {}
    mbti_list = []
    for n in mbti:
        if n in mbtis:
            mbtis[n] += 1
        else:
            mbtis[n] = 1
    for mbti, count in mbtis.items():
        mbti_list.append((mbti, count))
    mbti_list.sort(key=lambda x : (x[1], x[0]), reverse=True)
    min_ans = 12
    for i in range(len(mbti_list)):
        mbti, count = mbti_list[i]
        if count >= 3:
            ans = 0
        elif count == 2:
            ans = 8
            for j in range(i+1, len(mbti_list)):
                mbti2, count2 = mbti_list[j]
                if mbti != mbti2:
                    cnt = 0
                    for p in range(4):
                        if mbti[p] != mbti2[p]:
                            cnt += 2 # 첫번째, 두번째가 같은 사람이더라도 세번째가 다른 사람이면 첫번째 세번째 다른거랑, 두번째 세번째 다른거 2개씩 추가되어야 되니깐
                    ans = min(ans, cnt)
        elif count == 1:
            ans = 12
            for j in range(i+1, len(mbti_list)):
                mbti2, count2 = mbti_list[j]
                for k in range(j+1, len(mbti_list)):
                    mbti3, count3 = mbti_list[k]
                    if mbti != mbti2 and mbti != mbti3 and mbti2 != mbti3:
                        cnt = 0
                        for p in range(4):
                            if mbti[p] != mbti2[p]:
                                cnt += 1
                            if mbti2[p] != mbti3[p]:
                                cnt += 1
                            if mbti3[p] != mbti[p]:
                                cnt += 1
                        ans = min(ans, cnt)
        min_ans = min(ans, min_ans)
    print(min_ans)