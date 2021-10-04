import sys

### pypy
### 리스트복사아닌 변수사용 arr변경
### 조건 좀 잘봐 젭알,,,

n, m, r = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def spin(a, b, c, d):
    temp = arr[a][b]
    for i in range(a + 1, c):
        value = arr[i][b]
        arr[i][b] = temp
        temp = value

    for i in range(b + 1, d):
        value = arr[c - 1][i]
        arr[c - 1][i] = temp
        temp = value

    for i in range(c - 2, a - 1, -1):
        value = arr[i][d - 1]
        arr[i][d - 1] = temp
        temp = value

    for i in range(d - 2, b - 1, -1):
        value = arr[a][i]
        arr[a][i] = temp
        temp = value

    return None


for i in range(r):
    a, b, c, d = 0, 0, n, m
    for j in range(min(n, m) // 2):
        spin(a, b, c, d)
        a += 1
        b += 1
        c -= 1
        d -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()

