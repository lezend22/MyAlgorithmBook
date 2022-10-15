import sys
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
tmp = 'abcdefghijklmnopqrstuvwxyz'
tmp2 = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'
alp = {'a'}
ALP = {'A'}
for i in range(1, len(tmp)):
    alp.add(tmp[i])
    ALP.add(tmp2[i])

def show():
    for i in arr:
        print(i)
    print()

def dfs():
    ret = 0
    queue = deque()
    visited = {(0, 0)}
    queue.append((0, 0))

    while queue:
        x, y, = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and (nx, ny) not in visited:
                o_ = ord(arr[nx][ny])
                # 키가 없어 못 가는 곳일떄
                # 키가 있어서 열수 있는 문일때
                if chr(o_ + 32) in key:
                    # print(("SEX", arr[nx][ny]))
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    continue
                # 그냥 뚫린 벽일때
                if arr[nx][ny] == '.':
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    continue
                # 열쇠가 있는 곳일때
                if arr[nx][ny] in alp:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    key.add(arr[nx][ny])
                    continue
                # 서류가 있는 곳일때
                if arr[nx][ny] == '$':
                    # print("RET SEX", arr[nx][ny], nx, ny)
                    ret += 1
                    answer.add((nx, ny))
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    continue

    # print(key)
    return ret, len(key)



if __name__ == '__main__':

    t = int(sys.stdin.readline())
    for _ in range(t):

        n, m = map(int, sys.stdin.readline().split())
        arr = []
        tmp = ['.'] * (m+2)
        arr.append(tmp)
        for _ in range(n):
            l = list(map(str, sys.stdin.readline().rstrip()))
            l = ['.'] + l + ['.']
            arr.append(l)
        arr.append(tmp)

        key = set(map(str, sys.stdin.readline().rstrip()))

        cnt = 0
        pivotLen = 0
        answer = set()
        while True:
            c, keyLen, = dfs()
            if c == cnt and pivotLen == keyLen:
                break
            else:
                cnt, pivotLen = c, keyLen

        print(len(answer))