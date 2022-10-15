from collections import deque


def solution(queue1, queue2):

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    o1 = deque(queue1)
    o2 = deque(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    tmp = sum1 - sum2

    cnt = 0
    flag = False

    while tmp != 0:

        if not q1 or not q2:
            return -1

        if flag:
            if len(o1) == len(q1) and len(o2) == len(q2):
                if cnt > len(q1) + len(q2):
                    return -1

        flag = True
        if tmp > 0:
            popleft = q1.popleft()
            q2.append(popleft)
            tmp -= (popleft * 2)

        elif tmp < 0:
            popleft = q2.popleft()
            q1.append(popleft)
            tmp += (popleft * 2)

        cnt += 1

    answer = cnt
    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))