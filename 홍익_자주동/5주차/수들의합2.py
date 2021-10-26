# 기본적인 투포인터 문제
# 두개 포인터 시작점을 모두 리스트 처음으로 두고
# 조건에맞춰 앞뒤 포인터를 올려가며 리스트 맨마지막에 도달할때까지
# 경우의수 탐색
# 마지막 인덱스 범위만 주의하자
import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
i, j, count = 0, 0, 0


while i <= len(arr)-1 and j <= len(arr):
    if i == j:
        j += 1
    sum1 = sum(arr[i:j])
    if sum1 < m:
        j += 1
    elif sum1 > m:
        i += 1
    else:
        count += 1
        i += 1
        j += 1

print(count)
# 안좋은 예시,,사실상 O(n^2)이랑 다를게없음
# 심지어 중간에 큰수나오면 무한루프돔
# i, j = 0, len(arr)
# count = 0
#
# while i <= len(arr)-1:
#     sum1 = sum(arr[i:j])
#
#     for r in range(len(arr) - 1, i - 1, -1):
#         if sum1 > m:
#             # print("a")
#             sum1 -= arr[r]
#             continue
#         elif sum1 < m:
#             # print("b")
#             i += 1
#             break
#         else:
#             # print("c")
#             count += 1
#             i += 1
#             break
#
# print(count)
