import sys
from collections import deque

f1 = list(sys.stdin.readline().rstrip())
f2 = list(sys.stdin.readline().rstrip())
answer = []

f1.sort()
f2.sort(reverse=True)

queue1 = deque()
queue2 = deque()
for i in range((len(f1)+1)//2):
    queue1.append(f1[i])
for i in range(len(f2) // 2):
    queue2.append(f2[i])

back = []
for i in range(len(f1)):
    # 큐브러버 턴
    if i % 2:
        if not queue1 or queue1[0] < queue2[0]:
            popleft = queue2.popleft()
            answer.append(popleft)
        else:
            pop = queue2.pop()
            back.append(pop)
    # 구사과 턴
    else:
        if not queue2 or queue1[0] < queue2[0]:
            queue__popleft = queue1.popleft()
            answer.append(queue__popleft)
        else:
            queue__pop = queue1.pop()
            back.append(queue__pop)

back = back[::-1]
answer = answer + back
# print(answer + back)

print("".join(answer))

