import sys

conv = sys.stdin.readline().rstrip()

arr = list(map(str, conv.split(':')))
if len(arr) > 8:
    if arr[0] == '':
        arr = arr[1:]
    elif arr[-1] == '':
        arr = arr[:-1]
if len(arr) < 8:
    index = 0
    for i in range(len(arr)):
        if arr[i] == '':
            index = i

    while len(arr) < 8:
        arr.insert(index, '')
        # print("here")
for i in range(len(arr)):

    if 0 <= len(arr[i]) < 4:
        need = 4 - len(arr[i])
        for _ in range(need):
            arr[i] = '0' + arr[i]

for i in range(len(arr)):
    if i == len(arr)-1:
        print(arr[i])
    else:
        print(arr[i], end=':')

