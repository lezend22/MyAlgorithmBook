import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
arr = []
for _ in range(p):
    arr.append(int(sys.stdin.readline()))

answer = [0] * (g+1)
for i in range(p):
    lim = arr[i]
    flag = False
    for j in range(lim, 0, -1):
        if answer[j]:
            continue
        answer[j] = 1
        flag = True
        break

    if not flag:
        break

# print(answer)
print(sum(answer))
