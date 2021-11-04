# 맞왜틀?
# BOJ 20437
# 왜안돼진짜 어이없네
import sys
from collections import defaultdict

def stringGame(string, k):
    alpha = defaultdict(list)
    maximum = 0
    minimum = 10000

    for i in range(len(string)):
        if string.count(string[i]) >= k:
            alpha[string[i]].append(i)

    if not alpha:
        return (-1,)

    for i in alpha.values():
        for j in range(len(i)-k+1):
            temp = i[j+k-1] - i[j] + 1
            if temp < minimum:
                minimum = temp
            if temp > maximum:
                maximum = temp

    return minimum, maximum


t = int(sys.stdin.readline())
for _ in range(t):
    w = list(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline())
    print(*stringGame(w, k))


# t = int(sys.stdin.readline())
# for _ in range(t):
#     w = list(sys.stdin.readline().rstrip())
#     k = int(sys.stdin.readline())
#     word = []
#     count = [0] * 10001
#     length = []
#     for i in range(len(w)):
#
#         if w[i] not in word:
#             word.append(w[i])
#             index = word.index(w[i])
#             count[index] += 1
#
#         else:
#             index = word.index(w[i])
#             count[index] += 1
#             if count[index] == k:
#                 s = w.index(w[i])
#                 e = i
#                 length.append(e-s+1)
#                 count[index] -= 1
#                 w[s] = 0
#
#
#     if length:
#         print(min(length), max(length))
#     else:
#         print(-1)

