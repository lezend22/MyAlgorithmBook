import sys
from collections import deque

def solution(s):
    answer = []
    queue = deque(s)
    last = s[-1]
    for i in s:
        if i == last:
            queue.append(i)
            queue.popleft()
        else:
            break
    print(queue)

    count = 1
    popleft = queue.popleft()
    while queue:

        print("popleft", popleft)
        if popleft == queue[0]:
            count += 1
            queue.popleft()
        else:
            answer.append(count)
            count = 1
            popleft = queue.popleft()
            continue
    answer.append(count)

    answer.sort()
    return answer



solution("abca")