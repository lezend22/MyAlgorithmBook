# 가능한 단어 전부 뽑아보고
# sort()로 정렬 후 첫번째 요소 뽑기
# O(R*C*2),,,+ sort() O(nlogn)
# 더나은방법읍나?
import sys

r, c = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().rstrip() for _ in range(r)]
word = []
temp = ''
for i in range(r):
    for j in range(c):
        if arr[i][j] != '#':
            temp += arr[i][j]
        else:
            if len(temp) > 1:
                word.append(temp)
            temp = ''

    if len(temp) > 1:
        word.append(temp)
    temp = ''

for i in range(c):
    for j in range(r):
        if arr[j][i] != '#':
            temp += arr[j][i]
        else:
            if len(temp) > 1:
                word.append(temp)
            temp = ''
    if len(temp) > 1:
        word.append(temp)
    temp = ''

word.sort()
print(word[0])