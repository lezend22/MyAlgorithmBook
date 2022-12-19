from collections import deque

visited = []
room = []
def bfs(i):
    global visited, room

    queue = deque()
    queue.append(i)
    visited[i] = True

    while queue:
        popleft = queue.popleft()
        if not visited[room[popleft]]:
            queue.append(room[popleft])
            visited[room[popleft]] = True


def solution(rooms):
    global visited, room
    visited = [False] * (len(rooms) + 1)
    room = [0] + rooms

    cnt = 0
    for i in range(1, len(room)):

        if not visited[i]:
            bfs(i)
            cnt += 1

    # print(cnt)
    if cnt <= 2:
        return 1
    else:
        return cnt - 1

# print(solution(
# [1, 2, 3, 4, 5, 6]))
print(solution(
[3, 1, 2, 4]))