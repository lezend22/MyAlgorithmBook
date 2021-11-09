import sys


arr = [list(sys.stdin.readline().rstrip()) for _ in range(5)]
len1 = len(arr[1])

doyak = '.omln'
jump = 'owln.'
sit = '..oLn'


for j in range(len1):
    if arr[1][j] == 'o':
        for i in range(5):
            arr[i][j] = jump[i]
    elif arr[1][j] == 'w':
        for i in range(5):
            arr[i][j] = doyak[i]

for i in arr:
    print(''.join(i))