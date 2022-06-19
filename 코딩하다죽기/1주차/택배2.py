import sys

# 각 마을마다 이동가능한 블럭(C)를 설정하고
# 이동가능 한 수만큼 빼감
n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
arr = []
answer = 0
for i in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    arr.append((a, b, d))

# 도착점이 작은것 부터 정렬
# 시작점 < 도착점 이므로 먼저 도착할 수 있는 것부터 처리하는게 Greedy
truck = [c] * (n+1)
arr.sort(key=lambda x:x[1])


for s, e, p in arr:
    # 기준점 c 설정
    min_ = c
    for i in range(s, e):
        # s, e까지 중 제일 작은 값 탐색 후 저장
        min_ = min(truck[i], min_)
    # 탐색한 값과 p값 중에 더 작은것으로 저장
    pos = min(min_, p)
    for i in range(s, e):
        # 저장한 값을 s, e사이 모든 블럭에서 뺌
        truck[i] -= pos
    # answer에 이동한 상자 더함
    answer += pos
    # print(truck)

print(answer)
