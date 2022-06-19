
n, k = map(int, input().split())
arr = list(map(int, input().split()))
belt = []
for i in range(len(arr)):
    belt.append([arr[i], -1])


def rotate():
    temp = belt[-1]
    for i in range(len(belt)-1, -1, -1):
        if i == 0:
            belt[i] = temp
            break
        belt[i] = belt[i-1]

    if belt[n-1][1] == 1:
        belt[n-1][1] = -1

def putRobot():
    if belt[0][0] > 0:
        belt[0][0] -= 1
        belt[0][1] = 1

def robotMove():

    temp = [-1] * len(belt)
    for i in range(len(belt)-1, -1, -1):
        if belt[i][1] == 1:
            # print(i, belt[i])
            ni = (i+1) % (2*n)
            # print(ni)
            if belt[ni][0] > 0 and temp[ni] == -1:
                belt[ni][0] -= 1
                temp[ni] = 1
                temp[i] = -1
            else:
                temp[i] = 1
    # print(temp)
    for i in range(len(temp)):
        belt[i][1] = temp[i]

    if belt[n-1][1] == 1:
        belt[n-1][1] = -1

def check():
    cnt = 0
    for i in range(len(belt)):
        if belt[i][0] == 0:
            cnt += 1
    return cnt

stage = 0
while True:
    stage += 1
    # print("ssg", belt)
    rotate()
    # print("2", belt)
    robotMove()
    # print("3", belt)
    putRobot()
    # print("4", belt)
    cnt = check()
    if cnt >= k:
        print(stage)
        break
    # print("###########")