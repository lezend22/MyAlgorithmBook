import sys
import time

d = [0] * 100
n = int(sys.stdin.readline())


# ## 반복문 형식 (바텀업)
#
# d[0], d[ssg], d[2] = 0, ssg, ssg
#
# for i in range(3, n+ssg):
#     d[i] = d[i-ssg] + d[i-2]
#
# print(d[n])


## 재귀형식 (탑다운)

def pibo(x):
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

if __name__ == '__main__':
    print(pibo(n))