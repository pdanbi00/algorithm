# 문자열 비교랑 숫자 비교는 다름. 무튼 그래서 숫자가 1000이하라고 했으니깐
# 세자리까지 비교를 해보는거임 3, 30, 34가 있으면 이것들을 다 3번 곱하면
# 333, 303030, 343434 이렇게 되는데 이 상태에서 알아서 비교를 해줌.
# 그래서 정렬해서 순서대로 붙이되, numbers가 [0, 0] 인 경우는 문자열로 변환하면 00 이렇게 출력되기 떄문에 마지막에 int로 바꿨다가 다시 str로 출력
def solution(numbers):
    answer = ''
    numlist = list(map(str, numbers))
    numlist.sort(key = lambda x : x*3, reverse=True)
    for num in numlist:
        answer += num
    return str(int(answer))