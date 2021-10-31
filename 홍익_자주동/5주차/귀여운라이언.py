import sys

n, k = map(int, input().split())
dolls = list(map(int, input().split()))

answer = sys.maxsize

lion = []  # 라이언의 위치를 저장
for i in range(len(dolls)):
    if dolls[i] == 1:
        lion.append(i)

# 윈도우의 크기 = end - start = 라이언 인형의 개수
start = 0
end = k - 1

if len(lion) < k:
    print(-1)
    exit(0)

while True:
    # print(start, end)
    doll = lion[end] - lion[start] + 1
    answer = min(answer, doll)
    if end == len(lion) - 1:
        break
    start += 1
    end += 1
print(answer)