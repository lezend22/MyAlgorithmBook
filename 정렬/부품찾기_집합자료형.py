import sys

###집합자료형 사용

n = int(sys.stdin.readline())
array = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in arr2:
    if i in array:
        print('yes')
    else:
        print('no')

