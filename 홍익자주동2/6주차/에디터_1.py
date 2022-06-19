import sys

left = list(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline())
cnt = 0
right = []
while cnt < t:
    cnt += 1
    a = sys.stdin.readline().rstrip()
    # print(left, right, cnt)
    if a[0] == 'P':
        left.append(a[2])
    elif a[0] == 'L':
        # print("L")
        if left:
            right.append(left.pop())

    elif a[0] == 'D':
        if right:
            left.append(right.pop())

    elif a[0] == 'B':
        if left:
            left.pop()

left.extend(reversed(right))
print("".join(left))
