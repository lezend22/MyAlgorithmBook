
def swap(L, a, b):
    ret = False
    if L[a][0] >= L[b][0]:
        ret = True

    L[a], L[b] = L[b], L[a]
    return L, ret

def solution(L):
    L.sort(key=lambda x : (x[1], x[0]))
    p = 0
    while True:
        if p >= len(L):
            break

        a, b = L[p]
        cnt = 0
        for i in range(p-1, -1, -1):
            if L[i][0] >= a:
                cnt += 1
        # same
        if cnt == b:
            p += 1
            continue

        # print(p, cnt, b)
        k = p
        flag2 = False
        while cnt != b:
            flag2 = True
            if k <= 0:
                break
            # 클때
            if cnt > b:
                L, flag = swap(L, k-1, k)
                # print(L)
                if flag:
                    cnt -= 1
                k = k-1
                # print(k)

            # small
            if cnt < b:
                L, flag = swap(L, k, k+1)
                if flag:
                    cnt += 1
                k = k+1

        if not flag2:
            p -= 1
        p += 1

    answer = L
    return answer

print(solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))