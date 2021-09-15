import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().rstrip()))
count = 0
final = []

final.append(arr[0])
for i in range(1, len(arr)):
    if count == k:
        final = final + arr[i:]
        break

    final.append(arr[i])

    while len(final)>1:
        if count == k:
            break

        if final[-2] < final[-1]:
            final.pop(-2)
            count += 1
        else:
            break

while count < k:
    final.pop(-1)
    count+=1

for index in final:
    print(index, end='')
