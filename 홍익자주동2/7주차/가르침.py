import sys


n, k = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
result = 0

# 단어들 앞뒤 자르고 중간만 저장
for i in range(len(words)):
    words[i] = words[i][4:-4]

#k가 5보다 작으면 읽을수잇는거 한개도없음
if k < 5:
    print(0)
    exit(0)
if k == 26:
    print(n)
    exit(0)

result = 0
def dfs(idx, cnt):
    global result
    if cnt == poss:
        ret = 0
        for word in words:
            for w in word:
                if not letter[ord(w)-ord('a')]:
                    break
            else:
                ret += 1
        result = max(result, ret)
        return

    for i in range(idx, 26):
        if not letter[i]:
            letter[i] = 1
            dfs(i, cnt+1)
            letter[i] = 0

#공부헤야만하는 문자들 5개
prelearned = {'a', 'c', 't', 'i', 'n'}
letter = [0] * 26
for i in prelearned:
    if i in prelearned:
        letter[ord(i)-ord('a')] = 1
poss = k - 5
dfs(0, 0)

print(result)