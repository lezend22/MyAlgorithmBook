import sys

r, c, m = map(int, sys.stdin.readline().split())
arr = [[0] * c for _ in range(r)]
shark = [[] for _ in range(m)]
result = 0
catched = []

for i in range(m):
    a, b, z, d, e = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = (e, i)
    shark[i] = [a-1, b-1, z, d, e]
# print(shark)
def directionChange(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    elif d == 4:
        return 3

def sharkMove():
    #위 아래 오른쪽 왼쪽
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    nx, ny = -1, -1
    tempArr = [[0] * c for _ in range(r)]
    for i in range(len(shark)):
        print(i, "this shark", shark[i])
        if i in catched:
            continue
        #z 속력, d 이동방향, e 크기
        x, y, z, d, p = shark[i]
        print(i, "shark first pos", x, y)
        arr[x][y] = 0

        x += dx[d]
        y += dy[d]
        if 0 <= x < r and 0 <= y < c:
            pass

        else:
            x -= dx[d]
            y -= dy[d]
            directionChange(d)

        shark[i][0], shark[i][1], shark[i][3] = x, y, d
        print(i, "shark last pos", x, y)
        if tempArr[x][y]:
            if tempArr[x][y][0] < p:
                tempArr[x][y] = (p, i)
                catched.append(arr[x][y][1])
            else:
                catched.append(i)
        else:
            tempArr[x][y] = (p, i)

    return tempArr


def fish(idx):
    global result
    for i in range(r):
        if arr[i][idx] != 0:
            fishSize, sharkNum = arr[i][idx]
            result += fishSize
            arr[i][idx] = 0
            catched.append(sharkNum)
            return


if __name__ == '__main__':
    for i in range(c):
        fish(i)
        print("eaten", i, arr)
        arr = sharkMove()
        print("moved", i, arr)
    print(result)