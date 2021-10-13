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

