import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
real = [[] for _ in range(n)]

for i in range(len(arr)):

    memory = 0
    limit = arr[i]
    stack = []
    while True:

        if memory > limit:
            real[i+1] += stack

        a, b, c = map(str, sys.stdin.readline().split())
        b, c = int(b), int(c)

        if a == "I":
            memory += b
            stack.append((b, c))
            real[i].append((b, c))

        elif a == "F":
            find_ = real[i].index((b, c))
            print(i, find_)




