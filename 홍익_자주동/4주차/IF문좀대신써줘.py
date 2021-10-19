# 처음 딕셔너리 이용 그냥 구현했다가 틀림
# 10^5 개의 rate & 10^5개의 캐릭터의 개수
# + 오름차순이므로 이진탐색 사용해야함
# 이후 bs 재귀형으로 구현하였으나 recursive오류
# 항상 반복문 형으로 구현하자
# return result 변수 설정으로 if문 개수 줄임
import sys

n, m = map(int, sys.stdin.readline().split())
name = []
rate = []
for i in range(n):
    dname, drate = sys.stdin.readline().split(' ')
    name.append(dname)
    rate.append(int(drate))

def bsearch(arr, target):
    start, end = 0, len(arr)-1
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] >= target:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    return result

for i in range(m):
    num = int(sys.stdin.readline())
    b = bsearch(rate, num)
    print(name[b])
