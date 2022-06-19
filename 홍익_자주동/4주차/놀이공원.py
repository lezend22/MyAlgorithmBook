# 문제의 접근방법은 좋았지만
# 마지막 결과도출에서 애를 먹음
# 마지막 사람이 타는 놀이기구 번호를 출력
# 이분 탐색을 통해 마지막사람까지 탔을때 걸리는 분(min)값 구함
# 이후, 분(min)값을 통해 어느 놀이기구에서 마지막 사람이 걸리는지 확인
# 분(min)-ssg 까지의 시간까지 몇명 탔는지 확인 후, 1씩 더해가면서 어떤 놀이기구인지 찾아냄
import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
trace = False
result = 0
if n>m:
    s, e = 0, n*max(arr)
    while s<=e:
        count = 0
        mid = (s+e) // 2

        for i in arr:
            modulo = mid // i
            if modulo < 1:
                count += 1
            else:
                count += modulo
                if mid % i != 0:
                    count += 1

        if count >= n:
            e = mid - 1
            result = mid - 1
        else:
            s = mid + 1

    # print(result)
    total = m
    for i in range(m):
        total += (result-1) // arr[i]

    for i in range(m):
        if result % arr[i] == 0:
            total += 1
        if total == n:
            print(i+1)
            break

else:
    print(n)