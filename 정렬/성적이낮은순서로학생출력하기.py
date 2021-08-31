import sys

n = int(input())
arr = list()

for i in range(n):
    (name, score) = sys.stdin.readline().split()
    arr.append((name, int(score)))

arr.sort(key= lambda x:x[1])

for i in arr:
    print(i[0], end=' ')



###계수정렬이용

maximum = max(arr, key= lambda x:x[1])
size = int(maximum[1])

arr2 = [0] * (size+1)

for i in arr:
    arr2[i[1]] += 1

for i in range(len(arr2)):
    for j in range(arr2[i]):
        print(i ,end=' ')
