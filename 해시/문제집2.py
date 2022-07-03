import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
cnt = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    cnt[b] += 1

poss = []
for i in range(1, n+1):
    if cnt[i] == 0:
        heapq.heappush(poss, i)

answer = []
while poss:
    heappop = heapq.heappop(poss)
    answer.append(heappop)
    for i in graph[heappop]:
        cnt[i] -= 1
        if cnt[i] == 0:
            heapq.heappush(poss, i)

# for i in answer:
#     print(i, end=" ")
# print()

print(" ".join(map(str, answer)))