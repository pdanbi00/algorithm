# 노드에 부모노드 저장해두기
# 노드 a, b의 부모들을 거슬러 올라가면서 각각 배열에 저장
# 부모들 담은 배열 뒤에서부터 탐색하면서 부모가 달라지는 지점 직전이 가장 가까운 공통 조상

T = int(input())
for _ in range(T):
    N = int(input())
    graph = [0] * (N+1) # 노드 번호 별로 부모 노드 담기
    for _ in range(N-1):
        A, B = map(int, input().split())
        graph[B] = A
    a, b = map(int, input().split()) # a, b의 공통 조상을 구해야 됨.

    # a랑 b가 부모-자식 관계일 수 있어서 인덱스 에러 안나게 0 넣음
    a_parents = [0, a]
    b_parents = [0, b]

    while graph[a]:
        a_parents.append(graph[a])
        a = graph[a]

    while graph[b]:
        b_parents.append(graph[b])
        b = graph[b]

    # 뒤에서부터 탐색하면서 가장 가까운 공통 조상 찾기
    i = 1
    while a_parents[-i] == b_parents[-i]:
        i += 1

    print(a_parents[-i+1])