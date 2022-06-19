from collections import defaultdict

n, m, k = map(int, input().split())
# fireball = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
arr = [[[] for _ in range(n)] for _ in range(n)]
# print(arr)
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])
# print(arr)

def move():
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 0:
                for k in arr[i][j]:
                    m1, s1, d1 = k
                    # print(i, j, s1, d1)
                    nx = (n + i + dx[d1] * s1) % n
                    ny = (n + j + dy[d1] * s1) % n
                    temp[nx][ny].append([m1, s1, d1])

    return temp

def checkOddEven(checkList):

    ret = 2
    for i in checkList:
        if i[2] % 2 == 0:
            if ret == 1:
                return False
            ret = 0
        elif i[2] % 2 == 1:
            if ret == 0:
                return False
            ret = 1
    return True

def action():
    temp = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) > 1:
                nWeight, nSpeed, ndir = 0, 0, []
                for k in arr[i][j]:
                    m1, s1 ,d1 = k
                    nWeight += m1
                    nSpeed += s1
                nWeight = nWeight // 5
                if nWeight == 0:
                    continue
                nSpeed = nSpeed // len(arr[i][j])
                if checkOddEven(arr[i][j]):
                    ndir = [0, 2, 4, 6]
                else:
                    ndir = [1, 3, 5, 7]
                for t in range(4):
                    temp[i][j].append([nWeight, nSpeed, ndir[t]])
            else:
                # print("else:",arr[i][j])
                temp[i][j] = arr[i][j]

    return temp

def checkAns():
    ans = 0
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) == 0: continue
            for k in arr[i][j]:
                ans += k[0]

    return ans


cnt = 0
while cnt < k:
    # print(arr)
    arr = move()
    # print(arr)
    arr = action()
    # print(arr)
    cnt += 1
    # print("##########")

print(checkAns())
