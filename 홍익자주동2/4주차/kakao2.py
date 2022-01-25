import sys
import math

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
def checkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    convert = ''
    pj = n
    while pj > 0:
        rm = pj % k
        pj = pj // k
        convert += str(rm)

    convert = convert[::-1]
    # print(convert)
    ## count primeNum
    s, e = 0, 0
    prime = []
    while e < len(convert):
        if convert[s] == '0':
            s += 1
            e = s
            continue

        if e == len(convert)-1 and convert[e] != '0':
            # print("1here")
            # print(convert[s:e+1])
            prime.append(convert[s:e+1])

        if s != e and convert[e] == '0':
            # print("2here")
            # print(convert[s:e])
            prime.append(convert[s:e])
            s = e + 1

        e += 1
        # print(prime)

    # check it's prime num
    cnt = 0
    for i in prime:
        if i != '1' and checkPrime(int(i)):
            cnt += 1

    return cnt

print(solution(n, k))