import sys


n = int(sys.stdin.readline())
arr = list(sys.stdin.readline().rstrip())
visited = {'R' : 0, 'B' : 0}

visited[arr[0]] += 1

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        visited[arr[i]] += 1
print(min(visited['B'], visited['R'])+1)
