import sys
import time

d = [0] * 100
n = 99

### 반복문 형식 (바텀업)

d[1], d[2] = 1, 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])


### 재귀형식 (탑다운)

def pibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

if __name__ == '__main__':
    print(pibo(99))