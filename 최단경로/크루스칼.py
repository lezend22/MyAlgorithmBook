def find_set(x):
    # x의 대표원소를 찾아서 리턴한다.
    while x != parents[x]:
        x = parents[x]
    return x


"""
N: 정점의 개수 (0번 ~ N-1번)
M: 간선의 개수
edges: 그래프의 간선 정보
"""
def solution(n, weak, dist):
    edges = []
    pivot = weak[0]
    for i in range(1, len(weak)):
        leng = weak[i] - pivot
        edges.append((i - 1, i, leng))
        pivot = weak[i]

    # 간선을 비용순으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
    # cnt : 찾은 간선의 개수
    parents = [x for x in range(len(weak))]
    distance, cnt = 0, 0

    for a, b, value in edges:
        print(a, b, value)
        # 해당 간선이 사이클을 만들지 않는다면
        if find_set(a) != find_set(b):
            # union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
            parents[find_set(b)] = find_set(a)
            distance += value
            cnt += 1

            # N - 1개의 간선을 모두 찾은 경우, 탐색을 종료한다.
            if cnt >= n - 1:
                break

