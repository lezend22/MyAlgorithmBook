import sys
sys.setrecursionlimit(100000)
g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
arr = []
for _ in range(p):
    arr.append(int(sys.stdin.readline()))

parent = [x for x in range(g + 1)]
cnt = 0


def find_parent(x):
    global cnt
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    else:
        if parent[x] == 0:
            return -1
        parent[x] -= 1

    return parent[x]

cnt = 0
for i in range(p):
    answer = i
    # print("input", arr[i])
    ret = find_parent(arr[i])
    # print(ret)
    cnt += 1
    if ret == -1:
        cnt -= 1
        break

# print(parent)
print(cnt)
