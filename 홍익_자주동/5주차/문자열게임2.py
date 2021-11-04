# 맞왜틀?
# BOJ 20437
# 왜안돼진짜 어이없네
import sys
from collections import defaultdict
def string_game(string):
    len_str = len(string) # K개 이상 있는 문자만 따로 저장
    alpha = defaultdict(list)
    for i in range(len_str):
        if string.count(string[i]) >= K:
            alpha[string[i]].append(i)

    if not alpha:
        return (-1,)
    min_str = 10000
    max_str = 0
    for idx_lst in alpha.values():
        for j in range(len(idx_lst)-K+1):
            temp = idx_lst[j+K-1] - idx_lst[j] + 1
            if temp < min_str:
                min_str = temp
            if temp > max_str:
                max_str = temp
    return min_str, max_str

T = int(sys.stdin.readline())

for t in range(1, T+1):
    string = sys.stdin.readline().strip()
    K = int(sys.stdin.readline())
    print(*string_game(string))

# def stringGame(string, k):
#     alpha = defaultdict(list)
#     maximum = 0
#     minimum = 10000
#
#     for i in range(len(string)):
#         if string.count(string[i]) >= k:
#             alpha[string[i]].append(i)
#
#     if not alpha:
#         return (-1,)
#
#     for i in alpha.values():
#         for j in range(len(i)-k+1):
#             temp = i[j+k-1] - i[j] + 1
#             if temp < minimum:
#                 minimum = temp
#             if temp > maximum:
#                 maximum = temp
#
#     return minimum, maximum
#
#
# t = int(sys.stdin.readline())
# for _ in range(t):
#     w = list(sys.stdin.readline().rstrip())
#     k = int(sys.stdin.readline())
#     print(*stringGame(w, k))


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

