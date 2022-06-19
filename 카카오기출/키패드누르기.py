lx, ly = 3, 0
rx, ry = 3, 2

leftP = [1, 4, 7]
rightP = [3, 6, 9]
dic = {}
k = 1
for i in range(4):
    for j in range(3):
        dic[k] = (i, j)
        k += 1
dic[0] = (3, 1)

def checkDist(tx, ty, cx, cy):
    ret = abs(tx - cx) + abs(ty - cy)
    return ret

def checkHand(num, hand):
    global lx, ly, rx, ry

    if num in leftP:
        tx, ty, = dic[num]
        lx, ly = tx, ty
        return "L"
    elif num in rightP:
        tx, ty = dic[num]
        rx, ry = tx, ty
        return "R"
    else:
        tx, ty = dic[num]
        ld = checkDist(tx, ty, lx, ly)
        rd = checkDist(tx, ty, rx, ry)
        if ld < rd:
            lx, ly = tx, ty
            return "L"
        elif rd < ld:
            rx, ry = tx, ty
            return "R"
        elif ld == rd:
            if hand == 'right':
                rx, ry = tx, ty
                return "R"
            else:
                lx, ly = tx, ty
                return "L"


def solution(numbers, hand):
    answer = ''

    for i in numbers:
        answer += checkHand(i, hand)

    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))