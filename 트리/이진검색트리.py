import sys
sys.setrecursionlimit(10000)

cnt = 0
tree = []
while cnt < 10000:

    try:
        s = int(sys.stdin.readline())
        tree.append(s)
    except:
        break
    cnt += 1


def func(arr):
    # print(arr)
    if len(arr) < 1:
        return
    if len(arr) == 1:
        print(arr[0])
        return

    root = arr[0]
    ret = len(arr)
    for i in range(1, len(arr)):
        if arr[i] > root:
            ret = i
            break

    func(arr[1:ret])
    func(arr[ret:])
    print(root)

func(tree)

