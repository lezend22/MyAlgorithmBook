### BOJ 6416 RunTime ERROR
### 다시풀어!

from collections import deque
def verifyNode(arr):
    ### root is one
    start = []
    end = []
    root = []
    visited = []
    for i in range(len(arr)):
        start.append(arr[i][0])
        end.append(arr[i][1])
    for j in start:
        if j not in end and j not in root:
            root.append(j)
    if len(root) > 1:
        return False

    ### make tree & check only one incoming edge
    queue.append(root[0])
    while queue:
        v = queue.popleft()
        if v in visited:
            return False
        visited.append(v)
        for i in range(len(arr)):
            if arr[i][0] == v:
                queue.append(arr[i][1])



    ### verify loop node
    nodeNum = int(len(visited))
    if int(len(arr)) != nodeNum-1:
        return False

    return True


def getInput():
    arr = []
    while True:
        buf = input().rstrip().split("  ")

        if buf[0] == '':
            continue
        elif buf[0] == '-1 -1':
            global isWorking
            isWorking = False
            return False

        for i in buf:
            (a, b) = map(int, i.split(" "))
            if (a, b) == (0, 0):
                return arr
            else:
                arr.append((a,b))


if __name__ == '__main__':
    arrT = []
    isWorking = True
    queue = deque()

    while isWorking:
        v = getInput()
        if v == False:
            break
        arrT.append(v)

    if len(arrT) != 0:
        for i in range(len(arrT)):

            if arrT[i] == []:
                print("Case", i+1, "is a tree.")
            else:
                if verifyNode(arrT[i]) == True:
                    print("Case", i+1, "is a tree.")
                else:
                    print("Case", i+1, "is not a tree.")
