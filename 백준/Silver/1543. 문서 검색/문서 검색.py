line = list(input())
find = list(input())

ans = 0

idx = 0 # 문서의 철자 인덱스

for i in range(len(line)):
    # 중복되는 단어 포함하려고 할때는 건너뛰기
    if idx > i:
        continue
    # 찾는 단어와 문서의 단어가 같을때 정답 개수 추가
    if find == line[i:i+len(find)]:
        ans += 1
        # 인덱스 번호는 동시에 셀 수 없는 가장 가까운 번호로 이동
        idx = i + len(find)
                      
print(ans) 
