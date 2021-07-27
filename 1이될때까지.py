import sys

def mySol(N, K, count):
    while N != 1:
        if N % K == 0:
            N = N // K
            count += 1
        else:
            N -= 1
            count += 1
    print(count)


def greedySol(N, K):
    target = 0
    result = 0
    while True:
        target = (N//K)*K
        result += N - target    #1씩 계속 도는게아니라 한번에 뺴버림
        N = target
        if N < K:
            break   #더이상 나눗셈 불가 탈출

        result += 1
        N = N // K

    print(N)
    result += (N-1) #마지막 남은 수 1로 만들기 위한 빼기

    print(result)


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    count = 0
    mySol(N, K, count)
    greedySol(N,K)

