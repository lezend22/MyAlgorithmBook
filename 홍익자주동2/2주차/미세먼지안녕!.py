import sys

r, c, t = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cleaner = []
cnt = 0
result = 0

# print("초기")
# for i in arr:
#     print(i)
while True:

    spreadArr = [[0] * c for _ in range(r)]
    if t == cnt:
        break

    for x in range(r):
        for y in range(c):
            #공기청정기 확인
            if arr[x][y] == -1:
                cleaner.append((x, y))
            #미세먼지 확산
            if arr[x][y] != 0 and arr[x][y] != -1:

                spread = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        spread += 1

                        spreadArr[nx][ny] += (arr[x][y] // 5)
                arr[x][y] = (arr[x][y] - ((arr[x][y] // 5) * spread))

    for i in range(r):
        for j in range(c):
            arr[i][j] += spreadArr[i][j]

    # print("확산")
    # for i in arr:
    #     print(i)
    #공기 순환
    a, b = cleaner[0]
    a2, b2 = cleaner[1]
    temp, temp2 = 0, 0
    temp3, temp4 = 0, 0
    for i in range(c-1, 0, -1):
        if i == c-1:
            temp = arr[a][i]
            temp3 = arr[a2][i]
        if i == 1:
            arr[a][i] = 0
            arr[a2][i] = 0
        else:
            arr[a][i] = arr[a][i-1]
            arr[a2][i] = arr[a2][i-1]



    for i in range(a):
        if i == a-1:
            arr[i][c-1] = temp
        elif i == 0:
            temp2 =arr[i][c-1]
            arr[i][c-1] = arr[i+1][c-1]
        else:
            arr[i][c-1] = arr[i+1][c-1]

    for i in range(r-1, a2, -1):
        if i == r-1:
            temp4 = arr[i][c-1]
            arr[i][c-1] = arr[i-1][c-1]
        elif i == a2+1:
            arr[i][c-1] = temp3
        else:
            arr[i][c-1] = arr[i-1][c-1]

    for i in range(c-1):
        if i == 0:
            temp = arr[0][i]
            temp3 = arr[r-1][i]
            arr[0][i] = arr[0][i + 1]
            arr[r - 1][i] = arr[r - 1][i + 1]
        elif i == c-2:
            arr[0][i] = temp2
            arr[r-1][i] = temp4
        else:
            arr[0][i] = arr[0][i+1]
            arr[r-1][i] = arr[r-1][i+1]

    for i in range(a-1, 0, -1):
        if i == a-1:
            arr[i][0] = temp
        else:
            arr[i][0] = arr[i-1][0]

    for i in range(a2+1, r-1):
        if i == r-2:
            arr[i][0] = temp3
        else:
            arr[i][0] = arr[i+1][0]

    # print("순환")
    # for i in arr:
    #     print(i)
    cnt += 1

for i in arr:
    result += sum(i)
print(result+2)