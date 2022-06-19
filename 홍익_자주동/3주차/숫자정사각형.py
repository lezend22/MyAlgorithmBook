import sys

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

check = max(n, m)
result = 1
for i in range(n):
    for j in range(m):
        for k in range(check):
            if i+k<n and j+k<m and arr[i+k][j] == arr[i][j] and arr[i][j+k] == arr[i][j] and arr[i+k][j+k] == arr[i][j]:
                result = max(result, (k+1)*(k+1))
print(result)

# 모든 리스트 요소에 대해서 가로 세로 길이가
# 같은 것을 찾았는데 틀림
# 일단 단순하게 접근 최대 나올 수 있는 크기의
# 길이를 구하여 각 i, j에 k만큼 더하여 4꼭지점의
# 값이 전부 같은것을 찾음
# 너무 복잡하게 생각말고 리스트 범위에서 해결할 수 있게
# 꼭지점 4개만 생각해서 풀면됨

### 틀린코드
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
# result = []
# def check(i, j):
#     column, row = 0, 0
#     for a in range(i, n):
#         if arr[a][j] == arr[i][j]:
#             row = a
#     for b in range(j, m):
#         if arr[i][b] == arr[i][j]:
#             column = b
#     l1 = row - i + ssg
#     l2 = column - j + ssg
#     if l1 == l2 and arr[row][column] == arr[i][j]:
#         return (l1*l2)
#     return None
#
# for i in range(n):
#     for j in range(m):
#         p = check(i, j)
#         if p != None:
#             result.append(p)
# print(max(result))