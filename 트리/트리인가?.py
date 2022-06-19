import sys

index = 0
while True:

    index += 1
    edge = 0
    node = set()
    while True:

        flag = False
        s = sys.stdin.readline().rstrip()
        arr = list(map(str, s.split("  ")))
        if arr == ['']:
            continue
        for i in arr:
            a, b = map(int, i.split(" "))
            # print(a, b)
            if a == 0 and b == 0:
                flag = True
                break
            if a == -1 and b == -1:
                exit(0)
            edge += 1
            # print(edge)
            node.add(a)
            node.add(b)

    print(node, edge)
    if len(node) == 0:
        print("Case", index, "is a tree.")
        break

    if edge+1 != len(node):
        print("Case", index, "is not a tree.")

    if flag:
        break