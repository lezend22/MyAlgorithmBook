import sys

N, M, K = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

result = 0
totalSum = 0
arr.sort(reverse=True)

#sol1
while M >totalSum:
    r = 0
    while K > r and M > totalSum:
        result += arr[0]
        totalSum+=1
        r +=1

    result += arr[1]
    totalSum+=1

print(result)

#sol2
result = 0
first = arr[0]
second = arr[1]

count = int(M/(K+1) * K)
count += int(M % (K+1))

result += count * first
result += (M-count) * second

print(result)




