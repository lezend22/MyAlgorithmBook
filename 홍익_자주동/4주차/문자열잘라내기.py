# 2차원리스트이 세로 범위를 기준으로 이분탐색
# 이미 있는 word를 탐색하는 과정에서 trace boolean값을두고
# 중복여부를 확인, 중복일 시 end = mid - 1
# 중복아닐시, start = mid + 1로 최대값을 찾음
# 다만, 마지막에 중복일 시 mid값 반환할때 mid-1이 필요하므로
# 마지막 trace boolean값을 확인후 output처리시 확인
import sys

r, c = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(r)]
word = []
trace = True

def check1():
    global trace
    s, e = 0, r - 1
    result = 0
    while s <= e:
        mid = (s + e) // 2
        trace = True
        for i in range(c):
            temp = ''
            for j in range(mid, r):
                temp += arr[j][i]
            if temp in word:
                trace = False
                break
            word.append(temp)

        if trace:
            s = mid + 1
        else:
            e = mid - 1
        result = mid
    return result

mid = check1()

# mid가 중복이었을때
if not trace:
    print(mid - 1)
else:
    print(mid)

# def scount():
#     s, count = 0, -1
#     while s < r:
#         word = []
#         for i in range(c):
#             temp = ''
#             for j in range(s, r):
#                 temp += arr[j][i]
#             if temp not in word:
#                 word.append(temp)
#             else:
#                 return count
#         s += 1
#         count += 1
#     return count
#
# print(scount())
