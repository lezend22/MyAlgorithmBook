
def optSearchTree(n, p):
    A = [[0 for i in range(0, n+1)] for j in range(0, n+2)] #python에서 range는 1<= x < n이기때문에
    R = [[0 for i in range(0, n+1)] for j in range(0, n+2)]

    for i in range(1, n+1):
        A[i][i-1] = 0
        A[i][i] = p[i-1]
        R[i][i] = i
        R[i][i-1] = 0



    for diagnol in range(1, n):
        for i in range(1, n - diagnol + 1):
            j = i + diagnol

            minval = 999999

            for k in range(i, j+1):
                if(A[i][k-1] + A[k+1][j]) < minval:
                    minval = A[i][k-1]+A[k+1][j]
                    kValue = k

            R[i][j] = kValue

            sum_ = p[i-1]
            for s in range(i+1, j+1):
                sum_ = sum_ + p[s-1]
            A[i][j] = minval + sum_
    minavg = A[1][n]

    return A, R, minavg



if __name__ == '__main__':
    p = [0.05, 0.15, 0.05, 0.35, 0.05, 0.35]
    a, b, c = optSearchTree(6, p)
    print(a)
    print(b)
    print(c)