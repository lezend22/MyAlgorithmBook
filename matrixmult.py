import sys

d = [10, 4, 5, 20, 2, 50]
M = [[0 for x in range(6)] for y in range(6)]
P = [[0 for x in range(6)] for y in range(6)]


for diag in range(1, 5):
    for i in range(1, 6 - diag):
        j = i + diag
        M[i][j] = sys.maxsize
        for k in range(i, j):
            if(M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j] < M[i][j]):
                M[i][j] = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                P[i][j] = k

for i in range(1, 6):
    for j in range(1, 6):
        if M[i][j] == None:
            print(0, end=" ")
        else:
            print(M[i][j], end=" ")
    print()

print("here is List P")
for i in range(1, 6):
    for j in range(1, 6):
        if P[i][j] == None:
            print(0, end=" ")
        else:
            print(P[i][j], end=" ")
    print()
