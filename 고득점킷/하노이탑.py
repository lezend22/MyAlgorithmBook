import sys

n = int(sys.stdin.readline())
cnt = 0
path = []
def hanoi(num, from_, via_, to_):
    global cnt, path
    if num == 1:
        path.append((from_, to_))
        cnt += 1
    else:
        hanoi(num-1, from_, to_, via_)
        path.append((from_, to_))
        cnt += 1
        hanoi(num-1, via_, from_, to_)


hanoi(n, 1, 2, 3)
print(cnt)
if n <= 20:
    for a, b in path:
        print(a, b)
