# 아이디어 : orders 다 돌면서 문자열로 조합 만들어서 딕셔너리에 넣으면서 횟수 셈.
#           course 돌면서 딕셔너리 key의 길이가 course에 해당하는 값들 중 가장 횟수가 많은거를 result에 넣기 단, 횟수는 2이상
#           result는 알파벳 순으로 정렬해서 출력

from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course: # course 돌면서 길이가 k인 코스를 고름. 각 길이마다 최고 인기 있는거를 넣을거임
        new_course = {}

        for order in orders:
            order_list = list(''.join(order))
            for menu in combinations(order_list, k): # 메뉴로 알파벳  조합 만들기
                # print(menu) -> 이거 결과는 ('A', 'B') 이런식으로 나옴. 그래서 join 해줘야 됨.
                a = ''.join(sorted(menu)) # AB랑 BA 랑 같은거니까 정렬해서 join함.
                # 딕셔너리에 횟수 추가
                if a in new_course:
                    new_course[a] += 1
                else:
                    new_course[a] = 1
        # 딕셔너리 다 만들었으면 횟수가 2이상인 최고로 많이 나온것들을 result에 넣어주면 됨.
        for new_c in new_course: # 코스 길이가 k 인 조합들로 이뤄진 딕셔너리를 다 돌면서
            if max(new_course.values()) > 1: # 제일 많이 나온 것의 value값이 1 초과이면
                if new_course[new_c] == max(new_course.values()): # value 최고랑 일치하는 값들을 다 answer에 넣어준다.
                    answer.append(new_c)
    answer.sort() # 알파벳 오름차순으로 정렬하라 했으니깐
    return answer