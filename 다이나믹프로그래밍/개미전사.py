import sys
import time

#mySol
#대충 N * (N-2) = O(N^2-2N)이므로 매우 좋지 않음


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

start_time = time.time()
# d = [0] * 98
#
# for i in range(len(arr)):
#     if d[i] == 0:
#         d[i] = arr[i]
#     for j in range(i+2, n):
#         d[j] = d[i] + arr[j]
#
# print(max(d))


### 해답
# 점화식을 구해서 풀이 방법
d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n-1])

end_time = time.time()
print(end_time-start_time)

