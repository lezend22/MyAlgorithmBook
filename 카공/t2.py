
def solution(cap, n, deliveries, pickups):

    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    idx = 0
    m = 0

    while True:
        if idx >= n:
            break
        print("F", idx)
        print(deliveries)
        print(pickups)
        print(m, idx)
        m += 2 * (n - idx)
        pos1, pos2 = cap, cap
        i = idx
        while i < n:
            print("S", i)
            if pos1 and deliveries[i]:

                if deliveries[i] > cap:
                    rem = deliveries[i] // cap
                    deliveries[i] -= (cap * rem)
                    m += (rem-1) * (2 * (n - idx))
                    pos2 = cap * (rem)
                    pos1 = 0

                else:
                    pos1 -= deliveries[i]
                    deliveries[i] = 0

            if pos2 and pickups[i]:

                if pickups[i] > pos2:
                    pickups[i] -= pos2
                    pos2 = 0
                else:
                    pos2 -= pickups[i]
                    pickups[i] = 0

            if not (deliveries[idx] or pickups[idx]):
                idx += 1

            if not (pos1 or pos2):
                break

            i += 1

    print(m)

    return m

solution(2, 7, [1, 0, 2, 0, 1, 0, 6], [0, 2, 0, 1, 0, 2, 0])