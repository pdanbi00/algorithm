N, K = map(int, input().split())
nums = list(map(int, input().split()))

end = 0 # 마지막 지점 포인터
answer = 0 # 가장 긴 짝수로 이루어진 수열 길이
tmp = 0 # 현재 만들고 있는 가장 긴 짝수로 이루어진 연속 부분 수열 길이
odd = 0 # 안에 있는 홀수 개수

# start를 N까지 증가시키면서 반복
for start in range(N):
    # end를 가능한 만큼 이동시키기
    while (odd <= K and end < N):
    # while 문 탈출 기준이 count == K 가 아니라 count == K+1 이 되었을 때인 dldb :
    # 만약에 K = 2라면, 2개를 지우고 3개 째 지울 수 없을때의 짝수 부분 수열 길이를 출력해야해서.
        if nums[end] % 2 == 1: # 홀수
            odd += 1
        else: # 짝수
            tmp += 1
        end += 1

        if start == 0 and end == N:
            answer = tmp
            break
    if odd == K+1:
        answer = max(answer, tmp)
    # 다음 start로 넘어가기 전 작업
    if nums[start] % 2 == 1: # 시작점이 홀수라면
        odd -= 1
    else:
        tmp -= 1
print(answer)

